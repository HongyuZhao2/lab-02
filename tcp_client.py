"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
    
        message = input("Enter your message: ")
        sock.sendall(message.encode())
        data = sock.recv(256)
    
    print("Received Message: ", data)
    

if __name__ == '__main__':
    main()
