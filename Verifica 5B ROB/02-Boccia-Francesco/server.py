# FRANCESCO BOCCIA - 5BROB - 28/11/2024

import socket
import threading
import sqlite3


# gestisce la comunicazione con un client
def handle_client(conn, addr, client_id, operations):

    try:

        # cicla sulle operazioni assegnate al client
        for op in operations:

            # invia l'operazione al client
            conn.sendall(op.encode())

            # riceve il risultato calcolato dal client e lo stampa
            risultato = conn.recv(4096).decode()
            print(f"{op} = {risultato} from {addr[0]} - {addr[1]}")

        # invia un segnale di chiusura al client
        conn.sendall("exit".encode())

    except Exception as e:

        # gestisce eventuali errori durante la comunicazione
        print(f"Errore con il client {addr}: {e}")

    finally:

        # chiude la connessione al termine
        conn.close()


# funzione principale che avvia il server
def avvio_server():

    # si connette al database
    conn_db = sqlite3.connect("operations.db", check_same_thread=False)
    cur = conn_db.cursor()

    # recupera tutte le operazioni e i relativi client dal database
    cur.execute("SELECT client, operation FROM operations")
    data = cur.fetchall()
    conn_db.close()

    # divide le operazioni per ogni client
    operazioni_per_client = {}
    for client, operations in data:  #!!id client

        # se il client non è presente nella lista, lo aggiunge
        if client not in operazioni_per_client:

            operazioni_per_client[client] = []

        # aggiunge l'operazione alla lista del client
        operazioni_per_client[client].append(operations)

    # configura il socket del server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen()
    print("Server in ascolto...")

    client_id = 1

    try:

        while True:

            # accetta nuove connessioni dai client
            conn, addr = server.accept()
            print(f"Connessione accettata da {addr}")

            # controlla se ci sono operazioni per il client corrente
            if client_id in operazioni_per_client:

                client_ops = operazioni_per_client[client_id]

                # avvia un thread per gestire il client
                thread = threading.Thread(
                    target=handle_client, args=(conn, addr, client_id, client_ops)
                )
                thread.start()

                # incrementa l'ID per il prossimo client
                client_id += 1

    except KeyboardInterrupt:

        print("\nChiusura del server")

    finally:

        # chiude il socket del server al termine
        server.close()


if __name__ == "__main__":
    avvio_server()
