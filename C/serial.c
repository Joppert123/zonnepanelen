/*
 * serial.c
 *
 * Created: 31/10/2018 13:12:01
 * Author : Group 4
 *
 */ 

#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
#include <string.h>

void uart_init()
{
	// Setting baud rate 19.200
	UBRR0H = 0;
	UBRR0L = 51;
	// Disabling U2X mode
	UCSR0A = 0;
	// Enabling transmitter & receiver
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	// Setting frame format at asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

void serial_write(uint8_t data)
{
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A, UDRE0);
	
	// Writing data
	UDR0 = data;
}

void serial_writeln(const char* c)
{
	// Writing each character independently
	for (size_t i = 0; i < strlen(c); i++)
	{
		serial_write(c[i]);
	}
	
	// New line and carriage return
	serial_write(0x0A);
	serial_write(0x0D);
}

int serial_read()
{
	// Waiting until ready to transmit
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

int main()
{
	uart_init();
	_delay_ms(1000);
	
	char test1[] = "Protocol TODO.";
	
	while(1)
	{
		serial_writeln(test1);
		_delay_ms(1000);
	}
}