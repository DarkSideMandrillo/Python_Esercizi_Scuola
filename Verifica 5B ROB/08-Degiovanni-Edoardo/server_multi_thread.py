import socket
import sqlite3
import threading

host = "127.0.0.1"
porta = 9081
contatore_thread = 0  # variabile contatore che si occupa di contare i client


# funzione che gestisce il database e la sua query per ricevere le operazioni
def caricaOperazioni():
    conn = sqlite3.connect("operations.db")  # apro il DB
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, client, operation FROM operations"
    )  # viene eseguita la query che permette di salvarsi i dati del DB
    operazioni = cursor.fetchall()
    conn.close()
    return operazioni


def gestisciClienti(conn, ip_cliente, porta_cliente, operazioni, client_id):
    for id_operazione, client, operazione in operazioni:  # scorro le righe del database
        if (
            client == client_id
        ):  # se l'id del contatore (quindi id_cliente) è uguale a quello presente nel database allora gli invio l'operazione che è presente in quella riga
            # if "z" in operazione or "s" in operazione or "?" in operazione:
            #     break
            conn.sendall(operazione.encode())
            risultato = conn.recv(1024).decode()  # Riceve il risultato dal client
            print(
                f"{operazione} = {risultato} from {ip_cliente} - {porta_cliente}"
            )  # righa predefinita sul testo della verifica
    # quando la comunicazione sarà terminata allora il server invierà al client "exit" e termina la connessione con lui
    conclusione = "exit"
    conn.sendall(conclusione.encode())
    conn.close()


# funzione principale che si occupa della gestione del server_socket e dei Thread
def main():

    operazioni = (
        caricaOperazioni()
    )  # riceve le operazioni dalla funzione caricaOperazioni

    # gestione del socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, porta))
    server_socket.listen()  # di default dovrebbero essere 5 i client ammessi, perciò va bene

    while True:  # qua vengono gestiti correttamente i thread
        conn, (ip_cliente, porta_cliente) = server_socket.accept()
        #!! Non così sbagliato, ma da definire all'inizio del codice
        global contatore_thread  # soluzione (probabilmente non la più giusta) per permettere l'utilizzo della variabile contatore_thread all'interno del ciclo while
        contatore_thread += (
            1  # viene incrementata ogni volta che si esegue una connessione
        )
        client_id = contatore_thread  # incrementa il contatore dei client pareggiandolo a quello del thread, poteva essere utilizzato direttamente quello del thread
        thread = threading.Thread(
            target=gestisciClienti,
            args=(conn, ip_cliente, porta_cliente, operazioni, client_id),
        )
        thread.start()


if __name__ == "__main__":
    main()

# per quanto riguarda la gestione delle lettere contenute all'interno delle operazioni avevo pensato:

# if client == client_id:
#     if "a" in operazione: ...
#         break
#     conn.sendall(operazione.encode())
#     risultato = conn.recv(1024).decode()
#     print(f"{operazione} = {risultato} from {ip_cliente} - {porta_cliente}")
#
# però manca la parte di rimozione delle lettere all'interno delle operazioni
