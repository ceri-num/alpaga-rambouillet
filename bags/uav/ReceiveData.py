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

TIMER_PUMP = 20
TIMER_EV = 8

received_string = "void"
received_string_old = "not_void"

running_process = False

def waitProcess():
    global running_process
    wU = True
    while wU == True:
        if running_process == False :
            wU = False
            break
        time.sleep(0.1)

        print("test")
        print(running_process)

def data_receive_callback(xbee_message):
    global received_string, running_process

    received_string = xbee_message.data.decode()

    if received_string != "void" and received_string !="End":

        print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                            received_string))

        if(int(received_string) == 1):
            
            print("Activating the first EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV1, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV1, GPIO.HIGH)

        elif(int(received_string) == 2):
            print("Activating the second EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV2, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV2, GPIO.HIGH)

        elif(int(received_string) == 3):
            print("Activating the third EV!")
            GPIO.output(GPIO_PUMP, GPIO.HIGH)
            time.sleep(TIMER_PUMP)
            GPIO.output(GPIO_PUMP, GPIO.LOW)

            time.sleep(0.5)

            GPIO.output(GPIO_EV3, GPIO.LOW)
            time.sleep(TIMER_EV)
            GPIO.output(GPIO_EV3, GPIO.HIGH)

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

def main():
    global received_string, running_process, received_string_old

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

        device.add_data_received_callback(data_receive_callback)
        
        while (received_string != "End") :

            print("Waiting for data...\n")

            if(received_string != "void" and received_string_old != received_string and received_string !="End"):

                running_process = True

                waitProcess()

                print("Done")

                received_string_old = received_string

    finally:
        if device is not None and device.is_open():
            device.close()
        GPIO.cleanup()
        print("Close the communication with ground !")
        
if __name__ == '__main__':
    main()
