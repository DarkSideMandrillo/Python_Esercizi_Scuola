import socket
import threading
import sqlite3

# creo il socket del server
server_ip = "localhost"
port = 12345
address = (server_ip, port)


def gestisci_client(
    socket_client, indirizzo_client, operazioni, num_client, contatore_thread
):
    try:
        client_ip, client_port = indirizzo_client
        # scorro le operazioni ricevute dal client e controllo se siano uguali num_client del databse e contatore thread
        for i in range(len(num_client)):
            if num_client[i][1] == contatore_thread:
                operazione = operazioni[i][2]

                # invio l'operazione al client
                socket_client.send(operazione.encode())

                # ricevo il risultato dal client
                risultato = socket_client.recv(1024).decode()

                # stampo il risultato nel formato richiesto
                print(f"{operazione} = {risultato} from {client_ip} - {client_port}")

        # il server invia al client "esci" per terminare la connessione
        socket_client.send("esci".encode())

    except Exception as e:
        print(f"errore durante la gestione del client: {e}")

    finally:
        socket_client.close()


def carica_operazioni_dal_db(database):
    # effettuo la connesione al databse e creo il cursore per eseguire le operazioni
    connessione = sqlite3.connect(database)
    cursore = connessione.cursor()

    cursore.execute(
        "SELECT * FROM operation"
    )  # mi basta prendere solo la colonna operazioni
    operazioni = (
        cursore.fetchall()
    )  # uso la fetchall per ottenere tutte le tuple (righe)
    # cursore.execute("SELECT * FROM client") # mi basta prendere solo la colonna operazioni #!!??
    # num_client = cursore.fetchall() #uso la fetchall per ottenere tutte le tuple (righe)

    connessione.close()
    return operazioni, num_client


def avvia_server():  #!!err
    # creo il server, lo connetto e lo metto in asscolto
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)  #!! err
    server_socket.listen(5)

    # carico le operazioni con la funzione apposita e le memorizzo nella variabile operazioni
    operazioni, num_client = carica_operazioni_dal_db("operations.db")

    contatore_thread = 1
    # print("server in ascolto!")

    while True:
        # connessione con un client
        socket_client, indirizzo_client = server_socket.accept()

        # creo il thread per gestire il client e gli faccio eseguire gestisci_client
        thread_client = threading.Thread(
            target=gestisci_client,
            args=(
                socket_client,
                indirizzo_client,
                operazioni,
                num_client,
                contatore_thread,
            ),
        )

        thread_client.start()

        # incremento il contatore dei thread una volta che si connette un nuovo client per gestire le operazioni
        contatore_thread += 1


def main():
    avvia_server()


if __name__ == "__main__":
    main()
