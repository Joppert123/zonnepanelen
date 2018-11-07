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

void sunscreen_init()
{
	DDRD |= (1 << DDD7);
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

char sunscreen_extend()
{
	while (get_sonar_distance() < 50);
	PORTD |= (1 << PORTD7);
	return 1;
}

char sunscreen_retract()
{
	while (get_sonar_distance() > 2);
	PORTD &= ~(1 << PORTD7);
	return 1;
}