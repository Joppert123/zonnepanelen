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

#include <avr/eeprom.h>
#include <avr/io.h>
#include <stdio.h>

uint8_t EEMEM MIN_TEMP;
uint8_t EEMEM MAX_TEMP;

void analog_init()
{
	ADMUX = (1<<REFS0)|(1<<ADLAR);
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0); // Write | prescale 64
}

uint8_t get_min_temp()
{
	return eeprom_read_byte(&MIN_TEMP);
}

void set_min_temp(uint8_t length)
{
	eeprom_update_byte(&MIN_TEMP, length);
}

uint8_t get_max_temp()
{
	return eeprom_read_byte(&MAX_TEMP);
}

void set_max_temp(uint8_t length)
{
	eeprom_update_byte(&MAX_TEMP, length);
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

uint8_t get_temp()
{
	uint8_t mV = (read_adc(0) * (5000 / 1024)); //5V
	uint8_t temperature = ((mV * 100) / 1024);
			
	return temperature;
}

/*
	getLicht function
	@return void
	@see https://learn.adafruit.com/photocells/overview
*/

uint8_t get_light()
{
	
	uint8_t licht = read_adc(1);
	// < 10	DARK
	// 10 - 200 DIM
	// 200 - 500 LIGHT
	// 500 - 1000 VERY BRIGHT

	return licht;
}