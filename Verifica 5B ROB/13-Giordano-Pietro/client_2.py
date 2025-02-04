import socket

SERVER_ADDRESS = ('localhost', 2468)
BUFFER_SIZE = 4096

# Connette il client al server, riceve operazioni matematiche e invia i risultati
# Gestisce gli errori causati da operazioni non valide
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    while True:
        operation = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        
        if operation.lower() == "exit":
            print("Chiusura del client...")
            break

        try:
            result = str(eval(operation))
        except (SyntaxError) as e:
            # Gestisce errori per la sintassi interna al database in caso di operazione invalida, manda poi l'errore al server
            result = f"Errore: {e}"

        client_socket.sendall(result.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()