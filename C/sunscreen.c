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

#include "serial.h"

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
		return;
	}
	
	if (curr_temp > get_max_temp())
	{
		if (get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD5);
			PORTD |= (1 << PORTD7);
			auto_tempb = 1;
			return;
		}
		
		return;
	}
	
	if (curr_temp < get_min_temp())
	{
		if (get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD5);
			PORTD |= (1 << PORTD7);
			auto_tempb = 1;
			return;
		}
		
		return;
	}
	
	if (!get_sunscreen_status() && !manual)
	{
		PORTD &= ~(1 << PORTD7);
		PORTD |= (1 << PORTD5);
		auto_tempb = 0;
		serial_write(curr_temp);
	}
}

void auto_light()
{
	uint8_t curr_light = get_light();
	
	if (auto_tempb)
	{
		return;
	}
	
	if (curr_light > get_max_light())
	{
		if (get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD5);
			PORTD |= (1 << PORTD7);
			auto_lightb = 1;
			return;
		}
		
		return;
	}
	
	if (curr_light < get_min_light())
	{
		if (get_sunscreen_status() && !manual)
		{
			PORTD &= ~(1 << PORTD5);
			PORTD |= (1 << PORTD7);
			auto_lightb = 1;
			return;
		}
		
		return;
	}
	
	if (!get_sunscreen_status() && !manual)
	{
		PORTD &= ~(1 << PORTD7);
		PORTD |= (1 << PORTD5);
		auto_lightb = 0;
		serial_write(0x02);
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