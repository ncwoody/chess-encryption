import socket  # the socket library is used to send packets for ipv4, apparently

def sendchess(data):  # the data we are goint to send is supplied by the enc script
    addr = '127.0.0.1'  # the address we are going to send it to
    port = 10000  # the port we are going to send it to

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # this makes it udp
    soc.sendto(bytes(data, "utf-8"), (addr, port))  # this sends the message