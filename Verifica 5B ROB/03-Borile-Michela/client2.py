import socket

BUFFER_SIZE = 4092
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 6981))

while True:
    operation = client_socket.recv(BUFFER_SIZE).decode()

    if operation == "exit":
        break
    elif operation:
        result = str(eval(operation))
        client_socket.send(result.encode())
    else:
        print("errore")
        break

client_socket.close()

