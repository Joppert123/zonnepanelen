/*
 * serial.c
 *
 * Created: 06/11/2018 20:24:42
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#include "sonar.h"
#include "serial.h"

#include <avr/io.h>
#include <stdio.h>
#define F_CPU 16E6
#include <util/delay.h>
#include <avr/interrupt.h>

volatile char echoDone = 0;					// "Boolean" to check if echo is done
uint32_t countTimer0 = 0;					// 32-bit counter to save overflows from counter0

void sonar_init()
{
	DDRB |= (1 << PORTB0);					// Initializing HC-SR04 pins
	DDRB &= ~(1 << PORTB1);
}

uint16_t get_sonar_distance()
{
	float distance = 0.0f;
	uint16_t prevDist = 0.0;

	cli();									// Enabling echo-pin interrupt
	PCICR |= (1 << PCIE0);
	PCMSK0 |= (1 << PCINT1);
	sei();

	echoDone = 0;							// Reset echo
	countTimer0 = 0;						// Reset counter

	PORTB &= ~(1 << PORTB0);				// Setting trigger to high for 12us
	_delay_us(20);
	PORTB |= (1 << PORTB0);
	_delay_us(12);
	PORTB &= ~(1 << PORTB0);
	_delay_us(20);


	// --> INTERRUPT AREA <--


	while(!echoDone);						// Wait till echo is done

	PCICR &= ~(1 << PCIE0);					// Disabling echo-pin interrupt
	PCMSK0 &= ~(1 << PCINT1);

	float duration = countTimer0/16000000.0;	// 1:1 calculation

	distance = 17013.0 * duration;			// Distance in cm = duration in s * 340.26 * 100 * 1/2
	
	if (distance > 200)						// Sensor only works up to 400cm (Sunscreen is 2m)
	{
		distance = prevDist;
	}
	
	uint16_t convert = distance;			// Converting float to int
	return convert;
}

ISR(TIMER0_OVF_vect)
{
	countTimer0 += 255;						// Saving overflows to the 32-bit value
}

ISR(PCINT0_vect)
{
	if (PINB & (1 << PINB1))					// Start timer & overflow interrupt on rising edge
	{				
		TCCR0B |= (1<<CS00);
		TIMSK0 |= 1<<TOIE0;
	}
	else									// Falling edge
	{
		TCCR0B &= ~(1<<CS00);				// Stop timer
		countTimer0 += TCNT0;				// Save total counter value
		TCNT0 = 0;							// Reset timer
		echoDone = 1;						// Set echo to done
	}
}