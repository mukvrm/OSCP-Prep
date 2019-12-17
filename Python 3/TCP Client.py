# Goal 
# Client that starts a connection to the Python server
# and sends a message. Use function 'connect'

#import socket module 

import socket

CLT_ADDR = input("Type the IP address to use as source/client: ")
CLT_PORT = int(input("Type the TCP port you would like to connect to: "))

# Create new socket using the default family socket (AF_INET) that uses TCP
# the default scoket type connection-oriented (SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a remote socket at address

s.connect((CLT_ADDR, CLT_PORT))

# print Target IPv4 address and TCP port

print("Connected to:", CLT_ADDR,"on port:", CLT_PORT,"\n")

message = input("Enter message to send: ")

s.sendall(message.encode())
s.close()

