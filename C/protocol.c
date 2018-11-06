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

#include "serial.h"

#include <string.h>

void get_commands()
{
	char data[200];
	serial_readln(data, 200);
	
	// Commands
	if (!strcmp(data, "connect")) {
		data[0] = '\0';
		serial_writeln("Connected!");
	}
}