import socket as s
import sqlite3 as sql
import threading as t

SERVER_ADDRESS = ("0.0.0.0", 12345)
BUFFER_SIZE = 4096


def collega_db(db_path="operations.db"):
    """
    funzione che connette ad un db generico,
    di default usa operations.db per la consegna dell'esercizio
    se il db non esiste, questo viene creato
    """
    conn = sql.connect(db_path)
    curs = conn.cursor()
    return conn, curs


def chiudi_db(conn):
    """
    Chiude la connessione al database.
    """
    if conn:
        try:
            conn.close()
            print("Connessione al database chiusa con successo.")
        except Exception as e:
            print(f"Errore durante la chiusura della connessione: {e}")


def leggi_operazioni_per_client(curs):
    """
    funzione che legge il db e in base alla
    colonna del client popola un dizionario con chiave la chiave il numero del client
    """
    curs.execute(
        """
SELECT *
FROM operations"""
    )
    results = curs.fetchall()
    clients_operations = {}
    for x in results:  #!! un po superfluo
        if x[1] in clients_operations:
            clients_operations[x[1]].append(x[2])
        else:
            clients_operations[x[1]] = [x[2]]
    return clients_operations


def handle_client(client_socket, client_address, clients_operations, n, clients):
    """
    la funzione che viene utilizzata per gestire un thread,
    un client riceverà una stringa che è quella relativa al numero di client assegnato
    """
    operation_id = 0
    try:
        for index, operation in enumerate(clients_operations[n]):
            operation_id = index
            client_socket.send(operation.encode("utf-8"))
            risposta = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            print(risposta)
        client_socket.send("exit".encode("utf-8"))

    except s.timeout:
        if operation_id - len(clients_operations) < 0:
            clients[client_address].append(operation_id)
        print("Timeout scaduto")
    except s.error:
        if operation_id - len(clients_operations) < 0:
            clients[client_address].append(operation_id)
        print("errore del socket!!")
    finally:
        client_socket.close()


def start_server(clients_operations):
    server_operazioni = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_operazioni.bind(SERVER_ADDRESS)
    server_operazioni.listen(2)
    print("Server in ascolto...")
    clients = {}
    client_num = 1
    # server_operazioni.settimeout(10)
    clients
    while True:
        client_socket, client_address = server_operazioni.accept()
        if client_address in clients:
            client_thread = t.Thread(
                target=handle_client,
                args=(
                    client_socket,
                    client_address,
                    clients_operations,
                    clients[client_address],
                    clients,
                ),
            )
        else:
            clients[client_address] = [client_num, None]
            client_thread = t.Thread(
                target=handle_client,
                args=(
                    client_socket,
                    client_address,
                    clients_operations,
                    client_num,
                    clients,
                ),
            )
            client_num += 1
        client_thread.start()
        if len(clients.keys()) == len(clients_operations.keys()):
            break
    server_operazioni.close()


if __name__ == "__main__":
    conn, curs = collega_db()
    clients_operations = leggi_operazioni_per_client(curs)
    chiudi_db(conn)
    start_server(clients_operations)
    print(clients_operations)

# far partire dalla posizione in cui arriva lo stesso client
# gestire la disconnessione di un client
