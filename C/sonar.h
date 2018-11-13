/*
 * serial.h
 *
 * Created: 06/11/2018 20:24:42
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#include <avr/io.h>

#ifndef _sonar
#define _sonar

void sonar_init();
uint8_t get_sonar_distance();

#endif