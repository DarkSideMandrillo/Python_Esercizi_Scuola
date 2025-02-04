import socket

BUFFER_SIZE = 4092
#connessione al server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 6981))

while True:
    #mi salvo l'operazione da fare inviata dal server 
    operation = client_socket.recv(BUFFER_SIZE).decode()

    #se è exit vuol dire che le ho già fatte tutte ed esco così da chiudere la connessione
    if operation == "exit":
        break
    elif operation: #se l'operazione c'è, quindi non è vuota allora risolve l'operazione con eval e manda il risultato al server
        result = str(eval(operation))
        client_socket.send(result.encode())
    else:
        print("errore")  #se l'operazione è vuota da errore ed esce
        break

client_socket.close()

