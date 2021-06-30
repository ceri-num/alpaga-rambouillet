# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

#!/usr/bin/env python

import RPi.GPIO as GPIO

from digi.xbee.devices import XBeeDevice

# TODO: Replace with the serial port where your local module is connected to. 
PORT = "COM1"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

GPIO_EV1 = 11
GPIO_EV2 = 13
GPIO_EV3 = 15
GPIO_EV4 = 16

GPIO_PUMP = 18

def main():
    print(" +-----------------------------------------+")
    print(" | Xbee python software, receive data and activate relay according to the message |")
    print(" +-----------------------------------------+\n")

    GPIO.setwarnings(False)

    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    # set up the GPIO channels - one input and one output
    GPIO.setup(GPIO_EV1, GPIO.OUT)
    GPIO.setup(GPIO_EV2, GPIO.OUT)
    GPIO.setup(GPIO_EV3, GPIO.OUT)
    GPIO.setup(GPIO_EV4, GPIO.OUT)
    
    GPIO.setup(GPIO_PUMP, GPIO.OUT) 

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        def data_receive_callback(xbee_message):
            received_string = xbee_message.data.decode()

            print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                     received_string))

            if(int(received_string) == 1):
                GPIO.output(GPIO_EV1, GPIO.LOW)

            elif(int(received_string) == 2):
                GPIO.output(GPIO_EV2, GPIO.LOW)

            elif(int(received_string) == 3):
                GPIO.output(GPIO_EV3, GPIO.LOW)

            elif(int(received_string) == 4):
                GPIO.output(GPIO_EV4, GPIO.LOW)

        device.add_data_received_callback(data_receive_callback)

        print("Waiting for data...\n")

        input()

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
