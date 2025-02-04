import socket

SERVER_IP = 'localhost'  # IP del server
SERVER_PORT = 22222  # porta usata per la connessione
BUFFER_SIZE = 4096  # dimensione del buffer per i dati

# funzione principale del client (client si connette al server, invia id, riceve operazioni matematiche, 
# le calcola e invia i risultati al server)
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    client_id = input("Inserisci l'ID del client (1 o 2): ")
    client_socket.sendall(client_id.encode('utf-8')) # invia id

    try:
        while True:
            # riceve operazione dal server
            operazione = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if operazione == "exit": # se il server manda exit termino
                break  
            
            # calcolo risultato
            try:
                risultato = str(eval(operazione))  
            except Exception as e:
                risultato = f"Errore nell'operazione: {e}"

            client_socket.sendall(risultato.encode('utf-8')) # invio risultato al server
    except Exception as e:
        print(f"Errore nel client: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
