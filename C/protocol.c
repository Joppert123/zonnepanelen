/*
 * protocol.c
 *
 * Created: 05/11/2018 13:42:56
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#include "protocol.h"
#include "serial.h"
#include "sunscreen.h"
#include "sonar.h"
#include "analog.h"

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char connected = 0;

char get_connect_status()
{
	return connected;
}

void set_connect_status(char ack)
{
	connected = ack;
}

void get_commands()
{
	char data[200];
	char * split;
	uint8_t value;
	serial_readln(data, 200);
	
	// Split into value if SET command contains "="
	split = strtok(data, "=");
	split = strtok(NULL, "=");
	value = atoi(split);
	
	// CONNECTION
	if (!strcmp(data, "AAAAAA"))
	{
		data[0] = '\0';
		serial_write(0xAB);
		serial_write(0xCD);
		serial_write(0xEF);
		set_connect_status(1);
	}
	
	// SUNSCREEN GET
	if (!strcmp(data, "get_sunscreen_min_extend"))
	{
		data[0] = '\0';
		serial_write(get_sunscreen_min_extend());
	}
	if (!strcmp(data, "get_sunscreen_max_extend"))
	{
		data[0] = '\0';
		serial_write(get_sunscreen_max_extend());
	}
	if (!strcmp(data, "get_sunscreen_status"))
	{
		data[0] = '\0';
		sprintf(data, "%i", get_sunscreen_status());
		serial_writeln(data);
	}
	
	// SUNSCREEN SET
	if (!strcmp(data, "set_sunscreen_min_extend"))
	{
		data[0] = '\0';
		set_sunscreen_min_extend(value);
		serial_write(0xAA);
	}
	if (!strcmp(data, "set_sunscreen_max_extend"))
	{
		data[0] = '\0';
		set_sunscreen_max_extend(value);
		serial_write(0xAA);
	}
	if (!strcmp(data, "sunscreen_extend"))
	{
		data[0] = '\0';
		sunscreen_extend();
		serial_write(0xAA);
	}
	if (!strcmp(data, "sunscreen_retract"))
	{
		data[0] = '\0';
		sunscreen_retract();
		serial_write(0xAA);
	}
	
	// TEMPERATURE GET
	if (!strcmp(data, "get_min_temp"))
	{
		data[0] = '\0';
		serial_write(get_min_temp());
	}
	if (!strcmp(data, "get_max_temp"))
	{
		data[0] = '\0';
		serial_write(get_max_temp());
	}
	if (!strcmp(data, "get_temp"))
	{
		data[0] = '\0';
		serial_write(get_temp());
	}
	
	// TEMPERATURE SET
	if (!strcmp(data, "set_min_temp"))
	{
		data[0] = '\0';
		set_min_temp(value);
		serial_write(0xAA);
	}
	if (!strcmp(data, "set_max_temp"))
	{
		data[0] = '\0';
		set_max_temp(value);
		serial_write(0xAA);
	}
	
	// LIGHT GET
	if (!strcmp(data, "get_min_light"))
	{
		data[0] = '\0';
		serial_write(get_min_light());
	}
	if (!strcmp(data, "get_max_light"))
	{
		data[0] = '\0';
		serial_write(get_max_light());
	}
	if (!strcmp(data, "get_light"))
	{
		data[0] = '\0';
		serial_write(get_light());
	}
	
	// LIGHT SET
	if (!strcmp(data, "set_min_light"))
	{
		data[0] = '\0';
		set_min_light(value);
		serial_write(0xAA);
	}
	if (!strcmp(data, "set_max_light"))
	{
		data[0] = '\0';
		set_max_light(value);
		serial_write(0xAA);
	}
	
	// SONAR GET
	if (!strcmp(data, "get_sonar_distance"))
	{
		data[0] = '\0';
		serial_write(get_sonar_distance());
	}
}
