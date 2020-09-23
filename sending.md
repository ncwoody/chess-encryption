The packets python script adds a function that I made which will send the chess data over ip packets.
This uses the sockets library in python and sends UDP packets which each chess move in the data section of the packet.
Currently this sends to the loopback address (127.0.0.1) for testing purposes since this is just a proof of concept, but this can be changed easily.
I probably will do that eventually and I'll update when I do.
If you don't want to send packets, just comment out the line that calls sendchess() in the enc script.
