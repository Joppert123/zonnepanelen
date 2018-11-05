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

void test()
{
	serial_writeln("Testing scheduler!");
}

void setup()
{
	uart_init();
	sch_init_t1();
	
	sch_add_task(test, 0, 100);
	
	sch_start();
}

int main()
{
	setup();									// Setup of modules
	
	while (1)
	{
		sch_dispatch_tasks();	
	}
}