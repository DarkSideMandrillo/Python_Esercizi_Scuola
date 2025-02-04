import socket
import threading
import sqlite3
import time

# Funzione per gestire la connessione con un client
def handle_client(client_socket, client_ip, client_port, client_id):
    try:
        # Connessione al database SQLite
        conn = sqlite3.connect('operations.db')
        cursor = conn.cursor()
        # Seleziona le operazioni associate al client_id
        cursor.execute("SELECT operation FROM operations WHERE operations.id = ?", (client_id,))
        operations = [op for (op,) in cursor.fetchall()]
        conn.close()  # Chiude la connessione al database
        # Invia tutte le operazioni al client
        for operation in operations:
            client_socket.send(operation.encode())  # Invia l'operazione al client
            result = client_socket.recv(1024).decode()  # Riceve il risultato dal client
            print(f"{operation} = {result} from {client_ip} - {client_port}")  # Stampa il risultato ricevuto
            time.sleep(0.5)  # Ritardo per sincronizzare i messaggi
        # Dopo aver inviato tutte le operazioni, invia il messaggio "exit"
        client_socket.send("exit".encode())
    except Exception as e:
        # Gestisce eventuali eccezioni e stampa un messaggio di errore
        print(f"Errore con {client_ip}: {e}")
    finally:
        # Chiude la connessione socket con il client
        client_socket.close()

# Funzione per avviare il server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))  # Associa il server all'indirizzo localhost sulla porta 9999
    server.listen(5)  # Il server può gestire fino a 5 connessioni in coda 
    print("Server in ascolto...")
    while True:
        client_socket, addr = server.accept()  # Accetta la connessione di un client
        client_ip, client_port = addr  # Estrae l'indirizzo IP e la porta del client connesso      
        # Riceve l'ID del client inviato dal client stesso
        client_id = client_socket.recv(1024).decode()  # Riceve l'ID client
        # Crea e avvia un nuovo thread per gestire il client in modo indipendente
        thread = threading.Thread(target=handle_client, args=(client_socket, client_ip, client_port, int(client_id)))
        thread.start()  # Avvia il thread

if __name__ == "__main__":
    start_server()  # Avvia la funzione del server
