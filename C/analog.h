


/*
 * analog.c
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

uint8_t read_adc(uint16_t channel);
void getTemp();
void getLicht();



#endif /* ANALOG_H_ */
