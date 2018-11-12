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
#include "sonar.h"

#include <avr/io.h>
#include <avr/eeprom.h>

uint8_t EEMEM MIN_EXTEND;
uint8_t EEMEM MAX_EXTEND;

void sunscreen_init()
{
	DDRD |= (1 << DDD7);
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
	if (PORTD == (1 << PORTD7))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

void sunscreen_extend()
{
	while (get_sonar_distance() < get_sunscreen_max_extend());
	PORTD |= (1 << PORTD7);
}

void sunscreen_retract()
{
	while (get_sonar_distance() > get_sunscreen_min_extend());
	PORTD &= ~(1 << PORTD7);
}