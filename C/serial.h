/*
 * serial.h
 *
 * Created: 31/10/2018 13:12:01
 * Author : ITV2H - Groep 4
    ______                         __ __
  / ____/________  ___  ____     / // /
 / / __/ ___/ __ \/ _ \/ __ \   / // /_
/ /_/ / /  / /_/ /  __/ /_/ /  /__  __/
\____/_/   \____/\___/ .___/     /_/   
                    /_/            
 *
 */

#ifndef _serial
#define _serial

void serial_init();
unsigned char serial_read(void);
void serial_write(unsigned char data);
void serial_writeln(char* string);
void serial_readln(char *data, char size);

#endif