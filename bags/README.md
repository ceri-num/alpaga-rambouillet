This README.md is made to explain HOW TO USE THE BAGS SYSTEM CODE.
It will be constructed as a kind of procedure or tutorial that have to be follow for each flight.
Moreover it will focus on two different target, the UAV in the air and the GCS on ground.

GCS:
	-Switch on computer
	-Start a hotspot where the RPI will be connected automatically when it start
	-Connect the Xbee modem (configured before) corresponding to the GCS
	-Open a terminal :
		$cd /Git/alpaga-rambouillet/bags/gcs
		$python3 SendBroadcast.py
			+------------------------------------------------+
 			 | Xbee python software, send data to activate the relay according to the message  |
 			+------------------------------------------------+

			Enter the command to send to the Raspberry Pi in the UAV to activate the corresponding ElectroVane (1, 2, 3 or 4) :


		(At this point, wait until the UAV is ready!)

			Sending broadcast data: 3...
			Success

		(Command well send to the UAV)

			Enter the command to send to the Raspberry Pi in the UAV to activate the corresponding ElectroVane (1, 2, 3 or 4) :
			.
			.
			.

		(To quit the xbee link and the program, send "End instead of 1,2,3 or 4")

			End

UAV:
	-Prepare the mission before the flight (location, autorithy, insurance, ...)
	-Don't forget to charge the batteries of the UAV, the radiocommand and also the tablet !
	-Before to pack the UAV in the box, verify one last time the structure of the UAV ! Then pack it ! If you have a doubt, everythings can feat in the box (it is made for it)	

	-Once on the field, first evaluate the neighbouring and the possible obstacle in flight. Choose the launch and land location according to your observations. Remember, the two red motor correspond to the front of the UAV.
	-Prepare the drone. Get back the landing gear in place, put every batteries except one in the UAV and finally remove the propeller socket.
	-Have a quick "visual and touch" check of the propeller to be sure that everything is good. 

	-Attach the payload under the UAV without forgetting to connect the payload power supply (direct power from the UAV or battery). If the power supply of the payload is coming from the UAV, you can choose between the use of the power outlet under the UAV or directly disconnect the one from the landing gear and use it. If you do so, the landing gear will stay in the "down" position (which can be great to protect the payload)
	-Once the GCS is ready, take the radiocommand (RC) and connect the usb cable throught the RC to the tablet. Then power up the radiocommand (one short press then a second long one). Place the antenna in the good direction (targeting the sky).
	-Normally the application in the tablet will open itself. If not, click on the DJI PILOT application.
	-Once on the application, choose manual or mission flight. Before to fly the UAV, have a quick check of the different parameters of the drone. Check that the number of GPS sattellite are good, check that the IMU and other important sensors are well calibrated and finnaly have a quick look and modify (if necessary) the "Safety Height" or "Return To Home Altitude" and its strategies. 


	During the time where the pilot check the UAV state, the remote pilot can launch a second terminal on the GCS to connect it to the UAV RPI (this step is not necessary for the future but for now, it's important to have always the hand on the code running on the UAV in order to launch it back if it fails).

	Here is the second terminal on the GCS which correspond on the code running on the UAV's payload:
		$ssh ubuntu@M600PRO.local
		$passwrd : Drone
		$cd /Git/alpaga-rambouillet/bags/uav
		$python ReceiveData.py
			+-----------------------------------------+
			 | Xbee python software, receive data and activate relay according to the message |
			+-----------------------------------------+

			Waiting for data...
			Waiting for data...
			Waiting for data...
			.
			.
			.
			.
			Waiting for data...

		(At this point the UAV is waiting for instruction)

			From XX >> YY
			Activating the X EV!
			Running...
			Running...
			Running...
			.
			.
			.
			.
			Done

			Waiting for data...
			Waiting for data...
			Waiting for data...
			.
			.
			.

	It is possible, mainly because the code is not yet optimized, that the UAV programm crash. 
	It can stay in "Waiting for data..." mode until no end or it can also raise an error like this :
	ERREUR : digi.xbee.exception.XBeeException: Packet listener is not running.

	When these happens, keep the GCS code running and the UAV code windows opened. Open a third terminal :
		$ssh ubuntu@M600PRO.local
		$passwrd : Drone
		$ps aux
		...
		ubuntu    1475  4.0  0.1  23404  9908 pts/0    Sl+  04:55   0:00 python ReceiveD
		...
		$kill 1475

	Then relaunch the code in the UAV code windows. It's an hard solution but it still a good way to relaunch the code once the UAV is in flight.


POST FLIGHT LOG ANALYZES:
	Once the UAV back to the lab, you can easily dowload the UAV flight log where a lot of information are available.
	You can get this log on the tablet under the directory :
	/
	This log are sadly not readable for now because DJI encrypted them.
	To be usable, upload the log on this website : https://www.phantomhelp.com/LogViewer/Upload/?id=-3
	Once the log file upload, you can download other type of file.
	First you have the very interesting KML file which correspond to the GPS trajectory of the UAV. This one can easily been upload and seen in Google Eearth !!!
	The second file correspond to the information logged by the UAV in a readable text.
	The third file is the original one.