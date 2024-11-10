import sqlite3
import threading
import socket

def interrogation_db(data):
    conn = sqlite3.connect('file.db')
    data_parts = data.split("|")
    cur = conn.cursor()
    match int(data_parts[0]):
      case 1:
        SQL = """SELECT * FROM files WHERE nome=?"""
        cur.execute(SQL,(data_parts[1],))
      case 2:
        SQL = """SELECT tot_frammenti FROM files WHERE nome=?"""
        cur.execute(SQL,(data_parts[1],))
      case 3:
        SQL = """ SELECT frammenti.host
                  FROM files
                  JOIN frammenti ON files.id_file = frammenti.id_file
                  WHERE files.nome = ? AND frammenti.n_frammento = ?
                """
        cur.execute(SQL,(data_parts[1],data_parts[2]))
      case 4:
        SQL = """ SELECT frammenti.host
                  FROM files
                  JOIN frammenti ON files.id_file = frammenti.id_file
                  WHERE files.nome = ?
                """
        cur.execute(SQL,(data_parts[1],))

    result = cur.fetchall()
    print(result)
    conn.close()
    if not result:
      return "NO"
    return result


def handle_client(client_socket, client_address):
    print(f"Connesso a {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Ricevuto da {client_address}: {data.decode()}")
            response = interrogation_db(data.decode())
            print(response)
            response_str = '\n'.join([', '.join(map(str, row)) for row in response])
            client_socket.sendall(response_str.encode())
        except ConnectionResetError:
            break
    print(f"Connessione chiusa con {client_address}")
    client_socket.close()

def start_server(host='0.0.0.0', port=12345):
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind((host, port))
    tcp_server_socket.listen(10)  # Aumentiamo la coda a 10 connessioni
    print(f"Server in ascolto su {host}:{port}")

    # Ciclo per accettare continuamente connessioni
    while True:
        client_socket, client_address = tcp_server_socket.accept()
        print(f"Nuova connessione da {client_address}")
        # Crea un nuovo thread per ogni client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def main():
    start_server()

if __name__ == "__main__":
    main()
