/*
 * sunscreen.c
 *
 * Created: 07/11/2018 10:48:10
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#include "sunscreen.h"
#include "analog.h"
#include "sonar.h"

#include <avr/io.h>
#include <avr/eeprom.h>

uint8_t EEMEM MIN_EXTEND;
uint8_t EEMEM MAX_EXTEND;

char auto_tempb = 0;
char auto_lightb = 0;
char manual = 0;

void sunscreen_init()
{
	DDRD |= (1 << DDD7)|(1 << DDD6)|(1 << DDD5);
}

uint8_t get_sunscreen_min_extend()
{
	return eeprom_read_byte(&MIN_EXTEND);
}

void set_sunscreen_min_extend(uint8_t length)
{
	eeprom_update_byte(&MIN_EXTEND, length);
}

uint8_t get_sunscreen_max_extend()
{
	return eeprom_read_byte(&MAX_EXTEND);
}

void set_sunscreen_max_extend(uint8_t length)
{
	eeprom_update_byte(&MAX_EXTEND, length);
}

char get_sunscreen_status()
{
	if (PORTD == (1 << PORTD5))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

char get_sunscreen_manual()
{
	return manual;
}

void set_sunscreen_manual(char mode)
{
	manual = mode;
	
	if (mode)
	{
		PORTD |= (1 << PORTD6);
	}
	
	if (!mode)
	{
		PORTD &= ~(1 << PORTD6);
	}
}

void sunscreen_extend()
{
	//while (!(get_sonar_distance() == get_sunscreen_max_extend()));
	manual = 1;
	PORTD = 0b01100000;
}

void sunscreen_retract()
{
	//while (get_sonar_distance() > get_sunscreen_min_extend());
	manual = 1;
	PORTD = 0b01000000;
}

void auto_temp()
{
	uint8_t curr_temp = get_temp();
	
	if (auto_lightb)
	{
		return;			// If closed by other sensor do nothing
	}
	
	if (curr_temp > get_max_temp())
	{
		// Extend sunscreen when above maximum threshold temp
		if (!get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD7);		// Turn RED-LED off
			PORTD |= (1 << PORTD5);			// Turn GREEN-LED on
			auto_tempb = 0;
			return;
		}
		
		return;
	}
	
	if (curr_temp < get_min_temp())
	{
		// Retract sunscreen when under minimum threshold temp
		if (get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD5);		// Turn GREEN-LED off
			PORTD |= (1 << PORTD7);			// Turn RED-LED on
			auto_tempb = 1;
			return;
		}
		
		return;
	}
}

void auto_light()
{
	uint8_t curr_light = get_light();
	
	if (auto_tempb)
	{
		return;			// If closed by other sensor do nothing
	}
	
	if (curr_light > get_max_light())
	{
		// Extend sunscreen when above maximum threshold light
		if (!get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD7);		// Turn RED-LED off
			PORTD |= (1 << PORTD5);			// Turn GREEN-LED on
			auto_lightb = 0;
			return;
		}
		
		return;
	}
	
	if (curr_light < get_min_light())
	{
		// Retract sunscreen when under minimum threshold light
		if (get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD5);		// Turn GREEN-LED off
			PORTD |= (1 << PORTD7);			// Turn RED-LED on
			auto_lightb = 1;
			return;
		}
		
		return;
	}
}

void auto_sonar()
{
	if (get_sonar_distance() > get_sunscreen_max_extend())
	{
		PORTB |= (1 << PORTB2);
	}
	else if (get_sonar_distance() < get_sunscreen_min_extend())
	{
		PORTB &= ~(1 << PORTB2);
	}
}