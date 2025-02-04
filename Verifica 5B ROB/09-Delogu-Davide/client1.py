import socket

# Funzione principale per avviare il client
def start_client():
    # Crea un oggetto socket per la comunicazione TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))  # Connessione al server sulla porta 9999  
    client.send("1".encode())  # Invia l'ID del client al server 
    try:
        while True:  # Ciclo per ricevere e inviare operazioni fino a "exit"
            operation = client.recv(1024).decode()  # Riceve l'operazione dal server      
            # Se il server invia "exit", il client termina il ciclo
            if operation == "exit":
                break  # Esce dal ciclo e termina la connessione    
            try:
                result = eval(operation)  # Esegue l'operazione matematica ricevuta
                client.send(str(result).encode())  # Invia il risultato dell'operazione al server
            except Exception as e:
                client.send(str(e).encode())  # Invia un messaggio di errore al server    
    except ConnectionAbortedError as e:
        print(f"Errore di connessione: {e}")
    finally:
        client.close()  # Chiude la connessione con il server

if __name__ == "__main__":
    start_client()  # Avvia la funzione del client
