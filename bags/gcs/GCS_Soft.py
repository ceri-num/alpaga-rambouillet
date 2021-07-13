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

from digi.xbee.devices import XBeeDevice

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

DATA_TO_SEND = "Hello XBee!"
DATA_RCV = "void"

EV_STATE = ["Waiting", "Running", "Done"]

EV_STATUS = [EV_STATE[0]] * 4

def data_receive_callback(xbee_message):
	global DATA_RCV, EV_STATUS

	DATA_RCV = xbee_message.data.decode()

	# print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
 	#                            DATA_RCV))

 	if(DATA_RCV[0:4] == "ACKT"):

 		print("From %s >> Received Acknowledgement message ! Currently activating the electro valve : %i "; %(xbee_message.remote_device.get_64bit_addr(),
 																												DATA_RCV[8]))

 		if( EV_STATUS[int(DATA_RCV[8])-1] != EV_STATE[1] ):
 			EV_STATUS[int(DATA_RCV[8])-1] = EV_STATE[1]
	
 	elif(DATA_RCV[0:4] == "DONE"):

 		print("From %s >> Received Acknowledgement message ! Currently activating the electro valve : %i "; %(xbee_message.remote_device.get_64bit_addr(),
 																												DATA_RCV[8]))

 		if( EV_STATUS[int(DATA_RCV[8])-1] != EV_STATE[2] ):
 			EV_STATUS[int(DATA_RCV[8])-1] = EV_STATE[2]

def main():
	global DATA_TO_SEND, DATA_RCV, EV_STATUS

	print(" +------------------------------------------------+")
	print(" | Xbee python software, send data to activate the relay according to the message  |")
	print(" +------------------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)

	try:
		device.open()
        
		while DATA_TO_SEND != "End" :
        	
			new_data = input('Enter the command to send to the Raspberry Pi in the UAV to activate the corresponding ElectroVane (1, 2, 3 or 4) :')
			
			DATA_TO_SEND = new_data.rstrip("\n")
        	
			print("Sending broadcast data: %s..." % DATA_TO_SEND)

			device.send_data_broadcast(DATA_TO_SEND)

			print("Success")

			device.add_data_received_callback(data_receive_callback)

			print("Actual status of the electro valve :")
			print(EV_STATUS)

		print("Close the communication with UAV")

	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
	main()
