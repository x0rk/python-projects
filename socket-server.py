import socket
headersz = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.210.85",4545))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established")
	msg = "Hello my boy"
	msg = f'{len(msg):<{headersz}}' + msg
	clientsocket.send(bytes(msg,"utf-8"))
