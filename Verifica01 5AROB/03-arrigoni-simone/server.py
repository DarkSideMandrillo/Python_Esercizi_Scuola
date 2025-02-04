import threading
import socket
import sqlite3

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


class gestoreLivelloFiumi(threading.Thread):
    """classe thread che gestisce i client"""

    def __init__(
        self,
        connetion,
    ):
        super().__init__()
        self.connetion = connetion  # dichiarazione connessione
        self.id = self.connetion.recv(BUFFER_SIZE).decode()  # ricezione id server

    def run(self):
        message = self.connetion.recv(BUFFER_SIZE)  # ricezione messaggio con livello
        livello, data_ora = message.decode().split("|")  # split messaggio
        scorriDb(
            livello, data_ora, self.id, self.connetion
        )  # chiamata alla funzione che scorre il DB
        # print(data)


def scorriDb(livello, data_ora, id, connection):
    conn = sqlite3.connect("fiumi.db", check_same_thread=False)  # apertura del DB
    cur = conn.cursor()
    livello_int = float(livello)  # conversione a float del livello ricevuto dal client

    variabile_in_stampa = cur.execute(
        f""" SELECT *
                    FROM livelli
                    WHERE livelli.id_stazione = '{id}' """
    )  # select che prende i dati dal DB
    conn.commit()
    variabile_in_stampa = cur.fetchall()
    # print(variabile_in_stampa[0])
    tupla = variabile_in_stampa[0]  # variabile per calcolare il livello

    if tupla[3] > (
        livello_int * 0.3
    ):  # controllo se il livello ricevuto è minore del 30%
        connection.sendall("ricezione avvenuta".encode())
        print(f"fiume: {tupla[1]} in {tupla[2]} in data: {data_ora}")
    elif (tupla[3] <= (livello_int * 30) / 100) and (
        tupla[3] > (livello_int * 0.7)
    ):  # controllo se il livello ricevuto è magiore uguale del 30% e minore del 70%
        connection.sendall("ricezione avvenuta".encode())
        print(
            f"PERICOLO IMMINENTE al fiume: {tupla[1]} in {tupla[2]} in data: {data_ora}"
        )
    elif tupla[3] <= (  #!! basta else
        livello_int * 0.7
    ):  # controllo se il livello ricevuto è magiore uguale del 70%
        connection.sendall("richiesta attivazione sirena luminosa".encode())
        print(
            f"PERICOLO IMMINENTE al fiume: {tupla[1]} in {tupla[2]} in data: {data_ora}"
        )

    # print(variabile_in_stampa)
    conn.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creazione socket
    s.bind(MY_ADDRESS)  # associo l'ip al socket
    s.listen()  # aspetta che i server si colleghino
    while True:
        connetion, client_addres = s.accept()  # connessione del client al server
        print(f"il client: {client_addres} si è connesso")
        thread = gestoreLivelloFiumi(connetion)  # creazione thread
        thread.start()  # faccio partire il thread


if __name__ == "__main__":
    main()
