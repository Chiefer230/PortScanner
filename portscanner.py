import socket
import sys
from threading import Thread

"These Lists hold the ports that are scanned"
open_ports =[]
closed_ports = []

"Method used to scan a specific port using the sockets library. If there is a socket connection that is allowed then add to the open socket list and print the port number that is associated with that"
def scan_port(Target_port):
    global open_ports
    Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        Socket.connect((sys.argv[2],Target_port))
        Socket.close()
        print(f'{Target_port} is open')
        open_ports.append(Target_port)    
    except Exception:
        closed_ports.append(Target_port)
        pass

""
def check_ports():
    
    max_ports = 65535
    for i in range(1,max_ports):
        port_thread = Thread(target = scan_port, args=(i,))
        port_thread.start()
def print_result():
    print('results')


"This the Menu for now"
print(sys.argv[2])
if '-fs' in sys.argv[1] and '-o' in sys.argv[3]:
    check_ports()
    print(f'{open_ports} are all the Open Ports')