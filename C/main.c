/*
 * main.c
 *
 * Created: 05/11/2018 12:50:20
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
#include "scheduler.h"
#include "protocol.h"

#include <string.h>

void testing()
{
	serial_writeln("Arduino waiting?");
}

void setup()
{
	uart_init();								// Initializations
	sch_init();
	
	sch_add_task(testing, 0, 1000);				// Tasks
	sch_add_task(get_commands, 0, 1);			
	
	sch_start();								// Enable interrupts
}

int main()
{
	setup();									// Setup of modules
	
	while (1)
	{
		sch_dispatch_tasks();
	}
}