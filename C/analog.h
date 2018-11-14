/*
 * analog.h
 *
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#ifndef _ANALOG
#define _ANALOG

#include <stdint.h>

void analog_init();
uint8_t get_min_temp();
void set_min_temp(uint8_t length);
uint8_t get_max_temp();
void set_max_temp(uint8_t length);

uint8_t get_min_light();
void set_min_light(uint8_t length);
uint8_t get_max_light();
void set_max_light(uint8_t length);

uint8_t read_adc(uint16_t channel);
uint8_t get_temp();
uint8_t get_light();

#endif
