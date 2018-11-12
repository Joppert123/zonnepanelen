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

#include <string.h>
#include <stdio.h>

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
	serial_readln(data, 200);
	
	// CONNECTION
	if (!strcmp(data, "AAAAAA"))
	{
		data[0] = '\0';
		serial_write(0xAB);
		serial_write(0xCD);
		serial_write(0xEF);
		set_connect_status(1);
	}
	if (!strcmp(data, "ping"))
	{
		data[0] = '\0';
		serial_writeln("pong");
	}
	if (!strcmp(data, "get_connect_status"))
	{
		data[0] = '\0';
		sprintf(data, "%i", get_connect_status());
		serial_writeln(data);
	}
	
	// SUNSCREEN
	if (!strcmp(data, "get_sunscreen_status"))
	{
		data[0] = '\0';
		sprintf(data, "%i", get_sunscreen_status());
		serial_writeln(data);
	}
	if (!strcmp(data, "sunscreen_extend"))
	{
		data[0] = '\0';
		sprintf(data, "%i", sunscreen_extend());
		serial_writeln(data);
	}
	if (!strcmp(data, "sunscreen_retract"))
	{
		data[0] = '\0';
		sprintf(data, "%i", sunscreen_retract());
		serial_writeln(data);
	}
	
	// SONAR
	if (!strcmp(data, "get_sonar_distance"))
	{
		data[0] = '\0';
		sprintf(data, "%i", get_sonar_distance());
		serial_writeln(data);
	}
}