import socket

host = "0.0.0.0"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AAABBBCC",(host,port))

data, addr = client.recvfrom(4069)

print(data)
