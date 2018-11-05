/*
 * scheduler.h
 *
 * Created: 05/11/2018 13:15:04
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#ifndef _scheduler
#define _scheduler

// Scheduler data structure for storing task data
typedef struct
{
	void (* pTask)(void);			// Pointer to task
	unsigned int Delay;				// Initial delay in ticks
	unsigned int Period;			// Periodic interval in ticks
	unsigned char RunMe;			// RunMe flag
} sTask;

// Function prototypes
void sch_init_t1(void);
void sch_start(void);

// Core scheduler functions
void sch_dispatch_tasks(void);
unsigned char sch_add_task(void (*)(void), const unsigned int, const unsigned int);
unsigned char sch_delete_task(const unsigned char);

// Maximum number of tasks
#define SCH_MAX_TASKS (5)

#endif