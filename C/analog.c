/*
 * analog.c
 *
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */


#include "analog.h"
#include "serial.h"

#include <avr/io.h>
#include <stdio.h>
#define F_CPU 16E6
#include <util/delay.h>

void analog_init()
{
	ADMUX = (1<<REFS0)|(1<<ADLAR);
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0); // Write | prescale 64
}

/*
	read_adc function
	Analog to digital conversion
	@param  uint16_t analog channel
	@return uint8_t  adc value
*/



uint8_t read_adc(uint16_t channel)
{
		ADMUX &= 0xF0;							// Empty previous channel
		ADMUX |= channel;						// Admux => new channel
		ADCSRA |= (1<<ADSC);					// start conversion
		loop_until_bit_is_clear(ADCSRA, ADSC);
		return ADCH;
}

void getTemp()
{
		uint8_t mV = (read_adc(0) * (5000 / 1024)); //5V
		uint8_t temperature = ((mV * 100) / 1024);
		
			char buffer[5];
			sprintf(buffer, "%i", temperature);
			serial_writeln(buffer);
	
}

/*
	getLicht function
	@return void
	@see https://learn.adafruit.com/photocells/overview
*/

void getLicht()
{
	
	uint8_t licht = read_adc(1);
	// < 10	DARK
	// 10 - 200 DIM
	// 200 - 500 LIGHT
	// 500 - 1000 VERY BRIGHT
	
				char buffer[5];
				sprintf(buffer, "%i", licht);
				serial_writeln(buffer);
}



