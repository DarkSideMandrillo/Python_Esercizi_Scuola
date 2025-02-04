import socket
import threading
import sqlite3
import time


# Funzione per eseguire l'operazione matematica sul client
def handle_client(client_socket, client_address, operation):
    try:
        operation_exit = input("vuoi uscire, scrivi (si o no):")  #!! no
        if operation_exit == "no":
            client_socket.send(operation.encode())  # Invia l'operazione al client
            result = client_socket.recv(1024).decode()  # Ricevi il risultato dal client

            print(
                f"{operation} = {result} from {client_address[0]} - {client_address[1]}"
            )  # Stampa il risultato
        elif operation_exit == "no":
            client_socket.send(
                "exit".encode()
            )  # Per chiudere il collegamento invio exit
    except Exception as e:
        print(f"Errore durante la gestione del client {client_address}: {e}")
    finally:
        client_socket.close()  # Chiudi il socket del client


def main():
    conn_db = sqlite3.connect("operations.db")  # Connessione al database operations.db
    cursor = conn_db.cursor()
    cursor.execute(
        "SELECT * FROM operations"
    )  # Carica tutte le operazioni dal database operations.db
    operations = cursor.fetchall()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(
        ("localhost", 6981)
    )  # Indirizzo del server e porta su cui è connesso
    server_socket.listen(5)  # Il server rimane in ascolto
    print("Il server è in ascolto sulla porta 6981...")

    while True:
        client_socket, client_address = server_socket.accept()  # Accetta la connessione
        # Trova tutte le operazioni per il client specificato
        for op in operations:
            if op[1] == client_address[1]:  # Identifica il client per la porta
                operation = op[2]
                # Crea e avvia il thread per gestire il client
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(client_socket, client_address, operation),
                )
                client_thread.start()

        time.sleep(1)


if __name__ == "__main__":
    main()
