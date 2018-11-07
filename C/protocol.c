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

void get_commands()
{
	char data[200];
	serial_readln(data, 200);
	
	// --> COMMANDS <--
	if (!strcmp(data, "connect")) 
	{
		data[0] = '\0';
		serial_writeln("Connected!");
	}
	
	// SUNSCREEN
	if (!strcmp(data, "get_status"))
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
	if (!strcmp(data, "get_distance"))
	{
		data[0] = '\0';
		sprintf(data, "%i", get_sonar_distance());
		serial_writeln(data);
	}
}