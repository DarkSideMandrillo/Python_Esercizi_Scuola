import socket

# Configurazione del client
HOST = '127.0.0.1'  # Indirizzo del server
PORTA = 12345       # Porta del server

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: #creo un socket per la connessione
        client.connect((HOST, PORTA))
        
       
        while True:
            # Ricezione di un'operazione dal server
            operazione = client.recv(1024).decode()
            if operazione.lower() == "exit":
                print("Client 1 terminato") #il client si disconnette se c'è exit
                break

            try:
                risultato = eval(operazione) #ho utilizzato la funzione eval in graddo di ricevere un'operazione matematica
                client.sendall(str(risultato).encode())
            except Exception as e:
                client.sendall(f"Errore: {e}".encode()) # In caso di errore durante l'esecuzione di un'operazione, il client invia un messaggio di errore al server.

if __name__ == "__main__":
    start_client()