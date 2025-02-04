import socket
import threading
import sqlite3


# gestione del client
def handle_client(client_socket, client_address, operations):
    try:
        for operation in operations:
            # invio dell'operazione al client
            client_socket.send(operation.encode("utf-8"))

            # risposta del risultato da parte del client
            result = client_socket.recv(1024).decode("utf-8")
            print(
                f"{operation} = {result} from {client_address[0]} - {client_address[1]}"
            )

        # termino la connessione con il clien
        client_socket.send(b"exit")
    except Exception as e:
        print(f"erore nel gestire il client {client_address}: {e}")
    finally:
        client_socket.close()


def start_server():
    # connessione al database
    conn = sqlite3.connect("operations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT client, operation FROM operations")
    rows = cursor.fetchall()

    # assegnazione delle operazioni per client
    operations_per_client = {}
    for row in rows:
        client_id = row[0]
        operation = row[1]
        if client_id not in operations_per_client:
            operations_per_client[client_id] = []
        operations_per_client[client_id].append(operation)
    conn.close()

    # avvio del server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("server in ascolto sulla porta 9999...")

    # gestisco le connessioni con il client
    while True:
        client_socket, client_address = server.accept()
        print(f"connessione stabilita con: {client_address}")

        # identifico il client in base all'IP/porta
        client_id = len(operations_per_client)  #!! Cosi fa sempre la stessa
        if client_id in operations_per_client:
            client_operations = operations_per_client[client_id]
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address, client_operations),
            )
            client_thread.start()
        else:
            print(f"nessuna operazione disponibile {client_address}.")
            client_socket.close()


if __name__ == "__main__":
    start_server()
