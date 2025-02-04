import socket
import threading
import sqlite3

SERVER_ADDRESS = ('localhost', 2468)
BUFFER_SIZE = 4096

# Carica le operazioni dalla tabella `operations` del database SQLite
# Restituisce una lista di tuple (id, client, operation)
def carica_operazioni_da_DB():
    conn = sqlite3.connect("operations.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute("SELECT * FROM operations") 
    operazioni = cur.fetchall()
    conn.close()
    return operazioni

# Gestisce un client specifico, inviando le operazioni associate e ricevendo i risultati.
# Stampa i risultati delle operazioni sul server e salva i completamenti.
def handle_client(connection, id, operazioni):
    print(f"Connesso a client {id}")

    operazioni_client = [op for op in operazioni if op[1] == id]

    for operazione in operazioni_client:
        connection.sendall(operazione[2].encode('utf-8'))
        
        risultato = connection.recv(BUFFER_SIZE).decode('utf-8')

        salva_operazioni_completate(id, operazione[2], risultato)

        if "Errore" in risultato:
            print(f"Client {id}: {operazione[2]} ha generato l'errore: {risultato}")
        else:
            print(f"Client {id}: {operazione[2]} = {risultato}")
    
    try:
        connection.sendall("exit".encode('utf-8'))
    except:
        print(f"Impossibile inviare il comando 'exit' al client {id}")

    connection.close()
    
# Salva un'operazione completata in un file per poi riprendere in caso di chiusura della connessione di un client
def salva_operazioni_completate(client_id, operation, result):
    with open("operazioni_fatte.txt", 'a') as file:
        file.write(f"Client {client_id}: {operation} = {result}\n")              

# Avvia il server, carica le operazioni dal database e gestisce le connessioni client
def main():
    operazioni = carica_operazioni_da_DB()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen()

    print(f"Server in ascolto su {SERVER_ADDRESS}")

    contatore_thread = 0
    while True:
        conn, addr = server_socket.accept()
        contatore_thread += 1

        thread = threading.Thread(target=handle_client, args=(conn, contatore_thread, operazioni))
        thread.start()

if __name__ == "__main__":
    main()