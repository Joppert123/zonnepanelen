/*
 * serial.c
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

#include "serial.h"
#include <avr/io.h>
#include <string.h>
#include <avr/sfr_defs.h>

void uart_init()
{
	UBRR0H = 0;																// Setting baud rate 19.200
	UBRR0L = 51;
	UCSR0A = 0;																// Disabling U2X mode
	UCSR0B = _BV(TXEN0)  | _BV(RXEN0);										// Enabling transmitter & receiver
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);										// Setting frame format, 8 data bits, 1 stop bit
}

void serial_write(unsigned char data)
{
	while(!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}

void serial_writeln(char* string)
{
	for (size_t i = 0; i < strlen(string); i++)								// Writing each character independently
	{
		serial_write(string[i]);
	}
	
	serial_write(0x0A);														// New line and carriage return
	serial_write(0x0D);
}

unsigned char serial_read(void)
{
	while(!(UCSR0A & (1 << RXC0)));
	return UDR0;
}

void serial_readln(char *data, char size)
{
	unsigned char i = 0;
	
	if (!(UCSR0A & (1 << RXC0))) return;									// Don't wait for input, only when it happens
	
	if (size == 0) return;													// Return if not enough space in buffer

	while (i < size - 1)													// Check for space with NULL at the end
	{
		unsigned char c;
		c = serial_read();
		if (c == '\0') break;												// Break on null
		data[i] = c;														// Write into the buffer
		i++;
	}
	
	data[i] = 0;															// String null terminated
}