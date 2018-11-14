/*
 * sunscreen.h
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

#include <stdint.h>

#ifndef _sunscreen
#define _sunscreen

void sunscreen_init();
uint8_t get_sunscreen_min_extend();
void set_sunscreen_min_extend(uint8_t length);
uint8_t get_sunscreen_max_extend();
void set_sunscreen_max_extend(uint8_t length);
char get_sunscreen_status();
char get_sunscreen_manual();
void set_sunscreen_manual(char mode);
void sunscreen_extend();
void sunscreen_retract();
void auto_temp();
void auto_light();

#endif