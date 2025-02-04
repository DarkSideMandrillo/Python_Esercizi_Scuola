import socket
import threading
import sqlite3

# Indirizzo e porta su cui il server TCP sarà in ascolto
address = ("localhost", 8888)

# Creazione di un socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(address)  # Associa il socket all'indirizzo specificato
tcp_socket.listen(2)  # Il server ascolta fino a due connessioni

threads_started = []  # Lista per tracciare i thread avviati
dict = {"client_id": [], "operations": []}  # Dizionario per salvare dati dal database
first_client_operations = []  # Lista delle operazioni assegnate al primo client
second_client_operations = []  # Lista delle operazioni assegnate al secondo client


# Funzione main
def main():
    # richiama la funzione che legge il database e popola il dizionario `dict`
    read_database(dict)

    # estrazione delle operazioni per il primo client
    n_operations = 0  #!! No le operazioni devono essere infinite
    for id in dict["client_id"]:
        if id[0] == 1:  # Se il client_id è 1
            first_client_operations.append(dict["operations"][n_operations][0])
        n_operations += 1

    # estrazione delle operazioni per il secondo client
    n_operations = 0
    for id in dict["client_id"]:
        if id[0] == 2:  # Se il client_id è 2
            second_client_operations.append(dict["operations"][n_operations][0])
        n_operations += 1

    # Accetta la connessione dal primo client
    conn, addr = tcp_socket.accept()
    # Avvia un thread per gestire la connessione del primo client
    thread_first_client = threading.Thread(
        target=client_connection,
        daemon=True,
        args=(addr, conn, first_client_operations),
    )
    thread_first_client.start()
    threads_started.append(
        thread_first_client
    )  # Aggiunge il thread alla lista precedentemente dichiarata

    # Accetta la connessione dal secondo client
    conn, addr = tcp_socket.accept()
    # Avvia un thread per gestire la connessione del secondo client
    thread_second_client = threading.Thread(
        target=client_connection,
        daemon=True,
        args=(addr, conn, second_client_operations),
    )
    thread_second_client.start()
    threads_started.append(thread_second_client)  # Aggiunge il thread alla lista

    # Aspetta che tutti i thread terminino
    for thread in threads_started:
        thread.join()


# Funzione per gestire la connessione con il primo client
def client_connection(addr, conn, operations):
    try:
        n = 0
        for operation in operations:
            try:
                # Invia ogni operazione al client e riceve il risultato
                conn.send(operations[n].encode("utf-8"))  # Invio dell'operazione
                result = conn.recv(1024).decode("utf-8")  # Ricezione del risultato
                print(f"{operations[n]} = {result} from {addr[0]}-{addr[1]}")  # stampa
                n += 1
            except:
                print("Connessione terminata con il client per operazione non valida")
                break

        conn.send("exit".encode("utf-8"))  # Invia un comando di uscita al client
    except:
        pass


# Funzione per leggere i dati dal database SQLite
def read_database(dict):
    # Connessione al database SQLite
    conn = sqlite3.connect("operations.db")
    cur = conn.cursor()

    # Estrae i client_id dalla tabella 'operations'
    cur.execute("SELECT operations.client FROM operations")
    dict["client_id"] = cur.fetchall()

    # Estrae le operazioni dalla tabella 'operations'
    cur.execute("SELECT operations.operation FROM operations")
    dict["operations"] = cur.fetchall()

    conn.close()  # Chiude la connessione al database

    return dict


if __name__ == "__main__":
    main()
