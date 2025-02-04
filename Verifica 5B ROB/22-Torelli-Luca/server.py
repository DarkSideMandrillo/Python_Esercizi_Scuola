import socket
import sqlite3
import threading

server_address = ("127.0.0.1", 12345)
connected_clients = []  # lista di thread attivi
PATH_TO_DB = "./operations.db"
BUFFER_SIZE = 4096


def connect_to_db():
    """'
    Funzione per connettermi al db.

    Returns:
    cur -> cursore del db
    conn -> connessione al db
    """
    conn = sqlite3.connect(PATH_TO_DB)
    cur = conn.cursor()
    return cur, conn


def send_query(query, conn, cur):
    """
    funzione per inviare una query passata come argomento
    Parameters:
    query : string (quey da inviare al dbms)
    conn : connessione al db
    cur : cursore del db

    Returns:
    lista di tuple contenente i risultati della query
    """

    cur.execute(query)
    conn.commit()
    return cur.fetchall()


def read_operation(conn, cur):
    """
    Legge tutto il db, restituisce la query
    """
    query = f"""
            SELECT *
            FROM operations
            """
    return send_query(query, conn, cur)


def operation_by_client(datas, client_number):
    return_data = []
    for data in datas:
        if data[1] == client_number:
            return_data.append(data[2])

    return return_data


def handle_client(conn, client_address, datas, client_number):
    """
    ogni client viene gestito da un thead a sè,
    invio tutte le operazioni e quando finisco invio exit,
    il thread finisce quando viene deallocato quando viene effettuata
    la join nel main
    """
    operation_to_do = operation_by_client(datas=datas, client_number=client_number)
    for operation in operation_to_do:
        conn.send(operation.encode("utf-8"))
        response = conn.recv(BUFFER_SIZE).decode("utf-8")
        print(
            f"{operation} = {response} from {client_address[0]} - {client_address[1]}"
        )
    conn.send("exit".encode("utf-8"))


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(server_address)
    tcp_server_socket.listen(2)
    client_number = 0
    cur, conn_db = connect_to_db()
    datas = read_operation(conn=conn_db, cur=cur)
    conn_db.close()  # chiudo subito la connessione perchè i dati necessari li ho estratti tutti
    try:
        while (
            client_number < 2
        ):  # essendo due il numero massimo di client dentro il db quando arrivo al terzo client chiudo la connessione. #!!Serve un controllo migliore
            conn, client_address = tcp_server_socket.accept()
            client_number += 1
            connection = threading.Thread(
                target=handle_client, args=(conn, client_address, datas, client_number)
            )
            connection.start()
            connected_clients.append((connection, client_number))
    except (
        KeyboardInterrupt
    ):  # quando clicco ctrl C faccio la join di tutti i server e chiudo il socket
        print("Chiusura del server avviata dall'utente")
    finally:
        for connection in connected_clients:
            connection[0].join()  # riunisco tutti i thread
        tcp_server_socket.close()


if __name__ == "__main__":
    main()
