import socket

host = 'localhost'
port = 8888
client_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_tcp_socket.connect((host, port))

message = ''
while message != 'exit':
    message = client_tcp_socket.recv(1024).decode('utf8')
    try:
        operation = eval(message)
        print("L'operazione ricevuta è : {}".format(message))
        print("Il risultato dell'operazione è : {}".format(operation))
        client_tcp_socket.send(str(operation).encode('utf8'))
    except:
        print("Operation is not valid")
        break

print("Ricevuto exit...")
client_tcp_socket.close()
print("Terminata la connessione")