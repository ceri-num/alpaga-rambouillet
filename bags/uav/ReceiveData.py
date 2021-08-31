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

import time

# TODO: Replace with the serial port where your local module is connected to. 
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

GPIO_EV1 = 11
GPIO_EV2 = 13
GPIO_EV3 = 15
GPIO_EV4 = 16

GPIO_PUMP = 18

TIMER_PUMP = 3
TIMER_EV = 5

running_process = False

received_string = "void"

def data_receive_callback(xbee_message):
    global received_string, running_process

    received_string = xbee_message.data.decode()

    if(not running_process and received_string != "void"):

        print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                            received_string))

        running_process = True

        if(int(received_string) == 1):
            print("Activating the first EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV1, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV1, GPIO.HIGH)

            running_process = False
            received_string = "void"

        elif(int(received_string) == 2):
            print("Activating the second EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV2, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV2, GPIO.HIGH)

            running_process = False
            received_string = "void"

        elif(int(received_string) == 3):
            print("Activating the third EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV3, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV3, GPIO.HIGH)

            running_process = False
            received_string = "void"

        elif(int(received_string) == 4):
            print("Activating the fourth EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV4, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV4, GPIO.HIGH)

            running_process = False
            received_string = "void"

    else :
        print("Actually running on another electrovane!")

def main():
    global received_string

    print(" +-----------------------------------------+")
    print(" | Xbee python software, receive data and activate relay according to the message |")
    print(" +-----------------------------------------+\n")

    GPIO.setwarnings(False)

    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    # set up the GPIO channels - one input and one output
    GPIO.setup(GPIO_EV1, GPIO.OUT, initial = 1)
    GPIO.setup(GPIO_EV2, GPIO.OUT, initial = 1)
    GPIO.setup(GPIO_EV3, GPIO.OUT, initial = 1)
    GPIO.setup(GPIO_EV4, GPIO.OUT, initial = 1)
    
    GPIO.setup(GPIO_PUMP, GPIO.OUT, initial = 0) 

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        print("Waiting for data...\n")

        while received_string != "End" :

            device.add_data_received_callback(data_receive_callback)

        print("Close the communication with ground !")

    finally:
        if device is not None and device.is_open():
            device.close()
        GPIO.cleanup()
        
if __name__ == '__main__':
    main()