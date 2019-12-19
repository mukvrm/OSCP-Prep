import os
import socket
import platform

# Goal
# Build client and server that gets system information and
# list the content of a specific folder

# Listen on user provided IPv4 address // Alternatively, 
# SRV_ADDR = '' for it to use all available interfaces
# but it doesn't require user input

SRV_ADDR = input('Type IP to run server on: ')

# Listen on user provided port/TCP
# Alternatively, could be defined statically SRV_PORT = 5432

SRV_PORT = int(input('Type port/TCP to listen on: '))

# socket IPv4 and TCP - For server, must perform:
# the sequence socket(), bind(), listen(), accept()
# if more than one client, may need to repeat accept()
# more than once 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind function assigns user provided IP address and port to the socket

s.bind((SRV_ADDR, SRV_PORT))

# listen for incoming connections

s.listen(1)
print('Server started! Waiting for connections...')

# To accept a connection the socket must be bound to an address and 
# listening for connections. 
# The return value is a pair (conn, address) where conn is 
# a new socket object usable to send and receive data 
# on the connection, and address is the address bound to the socket 
# on the other end of the connection.

connection, address = s.accept()

# Print connection report including remote addr

print('Client ',address,'is c0nnected') 

# Print system information

print ('system: ', platform.architecture())

