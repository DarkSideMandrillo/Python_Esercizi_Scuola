import socket
import threading
import sqlite3

# Configurazione del server
HOST = "127.0.0.1"  # Indirizzo locale
PORTA = 12345  # Porta per il server


# è una funzione che serve per gestire un singolo client
def handle_client(conn, addr, client_id, operations):
    print(f"Connesso con {addr}")
    client_operations = [
        oper
        for oper in operazione
        if oper[1]
        == client_id  #!! non ho capito. Non funzionano così le litcomprehension
    ]  # Filtro le operazioni assegnate al client

    for operazione in client_operations:
        conn.sendall(operazione[2].encode())  # Invia l'operazione
        risultato = conn.recv(1024).decode()  # Riceve il risultato
        print(
            f"{operazione[2]} = {risultato} from {addr[0]} - {addr[1]}"
        )  # Stampo l'operazione, il risultato e l'indirizzo del client

    conn.sendall("exit".encode())  # Invio del comando di uscita al client
    conn.close()


# Funzione principale del server
def start_server():
    # Caricamento delle operazioni dal database
    conn_db = sqlite3.connect("operations.db")
    cursor = conn_db.cursor()
    # Creazione della tabella operations se non esiste, con chiave primaria id e client #!!Non devi creare nulla
    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS operations (
    id INTEGER PRIMARY KEY,
    client INTEGER NOT NULL,
    operation TEXT NOT NULL
);
"""
    )

    operations = cursor.fetchall()
    conn_db.close()

    # Configurazione del socket del server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORTA))
        server.listen()
        print(f"Il server è in ascolto su {HOST}:{PORTA}")

        while True:
            conn, addr = server.accept()
            client_id = (
                addr[1] % 2 + 1
            )  # Assegno client_id in base alla porta 1 o 2 #!! potrebbero esserci piu client
            # Creo e avvio un nuovo thread per gestire il client
            thread = threading.Thread(
                target=handle_client, args=(conn, addr, client_id, operations)
            )
            thread.start()


if __name__ == "__main__":
    start_server()
