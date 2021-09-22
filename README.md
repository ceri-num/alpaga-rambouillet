# alpaga-rambouillet

This git is made to gather every software component usefull for the project ALPAGA.
The aim of this work is to create and developp a new sampling method to collect a small volume of air in the atmosphere.
With the use of a DJI M600 PRO it is possible to embed a third party computer board on the payload in order to create interaction between the UAV flight controller and the electronic board thanks to ROS nodes.

The project is divided in two major part and in two different payload: the BAG system and the TUBE system. Each of them have a directory in the git repository.

The first one concern the development of a software architecture which allow the user to exploit the different ROS capacities of the DJI UAV. On this end, the architecture developped is based on the use of a Raspberry pi 3 or 4 (RPI3/4) and a Xbee Modem for the AIR-GROUND communication. The instructions for the payload is directly send from a computer on ground (Ground Control Station - GCS) to the UAV with a particular protocol. That's why you can find two different code on this git, one for the GCS and one to run on the UAV.

The second part concern the development of the payload itself. A big work of this project was on the construction of this payload that will allow a user to collect small volume of air at different altitude and different position. The first intention was to compare an existing payload based on TUBE to our created solution. At the end, the BAG system was ready to be tested but the TUBE system was still in construction. That's the reason why you will (for now) only find one directory, the one corresponding to the BAG system.

Directory Architecture :
/alpaga-rambouillet
	--> /bags
		README.md
		--> /gcs
			README.md
			CodeGCS.py
		--> /uav
			README.md
			CodeUAV.py
	--> /tube

PS: You will find several README.md in this architecture. First you will find one at the root of every system directory which will explain you how to use this code to command the UAV. The others README.me are place in subdirectory where the code are located. This one explain basically how the code is working.

PSi : The password of the RPI is "Drone"