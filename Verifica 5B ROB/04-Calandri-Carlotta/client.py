import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=("localhost", 6981)

client_socket.connect(server_address)
while True:
    # Ricevi l'operazione dal server
    operation = client_socket.recv(1024).decode()
    
    if operation == "exit":
        #nel caso in cui il client riceva dal server l'operazione di exit
        break
    
    # Calcola il risultato dell'operazione
    else:
        result = str(eval(operation))
        # Invia il risultato al server
        client_socket.send(result.encode())
    client_socket.close()