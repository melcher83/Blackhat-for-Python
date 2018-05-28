import socket

target_host ="127.0.0.1"
target_port = 9999


#create socket object

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect

client.connect((target_host,target_port))

#send data

client.send("ABCD")

#receive

response = client.recv(4096)
print response