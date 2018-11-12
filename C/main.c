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

#include "analog.h"
#include "serial.h"
#include "sonar.h"
#include "scheduler.h"
#include "protocol.h"
#include "sunscreen.h"

void setup()
{
	// Initializations
	analog_init();
	serial_init();
	sonar_init();
	sunscreen_init();
	sch_init();
	
	// Tasks
	sch_add_task(get_commands, 0, 1);
	
	// Enable
	sch_start();
}

int main()
{
	setup();
	
	while (1)
	{
		sch_dispatch_tasks();
	}
}
