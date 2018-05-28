import socket

target_host ="cbtvoice.bluewiretech.com"
target_port = 9000


#create socket object

client= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



#send data

client.sendto("AAABBBCCC",(target_host,target_port))

#receive

data, addr = client.recvfrom(4096)
print data