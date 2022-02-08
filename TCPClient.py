import socket

host = "bing.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket object

client.connect((host,port)) #connect the client

client.send("GET / HTTP/1.1\r\nHost: bing.com\r\n\r\n".encode(encoding='utf-8')) #send data with encoding

response = client.recv(4096) #Receive response

print (response) #print response
