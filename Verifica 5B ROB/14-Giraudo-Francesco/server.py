import socket
import threading
import sqlite3

# Funzione per gestire ciascun client
def handle_client(client_socket, client_address, operations, client_id):
    try:
        # Filtra le operazioni per il client specifico
        client_operations = [op for op in operations if op["client"] == client_id]
        for op in client_operations:
            operazione = op["operation"]
            client_socket.sendall(operazione.encode())  # Invia l'operazione
            risultato = client_socket.recv(4096).decode()  # Riceve il risultato
            print(f"{operazione} = {risultato} from {client_address[0]}:{client_address[1]}")
        
        # Invia il comando per terminare
        client_socket.sendall("exit".encode())
    except Exception as e:
        print(f"Errore durante la gestione del client {client_address}: {e}")
    finally:
        client_socket.close()

# Funzione per caricare operazioni dal database
def load_operations(database):
    try:
        conn = sqlite3.connect(database, check_same_thread=False)
        cur = conn.cursor()
        cur.execute("SELECT * FROM operations")
        records = cur.fetchall()
        conn.close()
        # Converte i dati del database in un elenco di dizionari
        operations = [{"id": r[0], "client": r[1], "operation": r[2]} for r in records]
        return operations
    except sqlite3.Error as e:
        print(f"Errore nel caricamento del database: {e}")
        return []

# Configurazione del server
def main():
    HOST = '127.0.0.1'
    PORT = 65432

    # Carica operazioni
    operations = load_operations("./operations.db")
    if not operations:
        print("Nessuna operazione caricata. Controlla il database.")
        return

    # Crea il socket del server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    thread_counter = 1
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            # Avvia un thread per gestire il client
            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address, operations, thread_counter),
            )
            thread.start()
            thread_counter += 1
    except KeyboardInterrupt:
        print("\nChiusura del server.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
