import socket
import threading
import sqlite3

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
NOME_DATABASE = "fiumi.db"

"""
FORMATO MSG da client= lvl_misurato|data&ora|id_stazione
FORMATO MSG per client= dati|attiva o disattiva sirena

"""


class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
        self.id_stazione = None  # inizializza questi dati a none, perche si ricevono al primo messaggio
        self.data = None
        self.livello_acqua = None
        self.msg_x_client = "Errore nel messaggio"  # inizia dicendo che c'è un errore poi se non ce ne sono viene assegnato il msg giusto, altrimenti il msg mandato dal client era sbagliato

    def run(self):
        while self.running:
            message = self.connection.recv(BUFFER_SIZE)
            print(message.decode())
            lista_msg = message.decode().split("|")
            if (
                len(lista_msg) == 3 and lista_msg[0] and lista_msg[1] and lista_msg[2]
            ):  # controlla che la lunghezza sia uguale a 3 e ciascun elemento non sia null
                # splitto il messaggio e salvo i dati negli attributi del thread
                self.livello_acqua = float(lista_msg[0])
                self.data = lista_msg[1]
                self.id_stazione = int(lista_msg[2])
                self.calcola_msg_client()

            self.connection.sendall(self.msg_x_client.encode())

    def calcola_msg_client(self):
        """
        Funzione che apre il db, con una query prende i dati dal db per confrontare lvl_misurato con lvl di guardia.
        In base al rapporto tra lvl misurato e di guardia viene creato un messaggio da inviare al client
        """
        # apro temporaneamente connessione con costrutto with per prendere dati da db. si chiude in automatico
        with sqlite3.connect(
            NOME_DATABASE
        ) as connessione:  #!! apro la connessione ogni volta
            cursore = connessione.cursor()
            cursore.execute(
                f"SELECT livello, fiume, localita FROM livelli WHERE id_stazione = {self.id_stazione}"
            )  # SELECT che prende i dati dal db in base alla stazione

            risultati = cursore.fetchall()
        if risultati:
            print(risultati)

            # salvo i dati presi con la query in variabili
            lvl_guardia = float(risultati[0][0])
            nome_fiume = risultati[0][1]
            localita_fiume = risultati[0][2]

            print(
                f"RICEVUTO MESSAGGIO DA: {nome_fiume}, LOCALITA: {localita_fiume} IN DATA E ORA: {self.data}"
            )  # IN tutti i casi stampo un msg in console  con nome, localita e data

            if (
                self.livello_acqua > lvl_guardia * 0.7
            ):  # ultimo  caso  manda ricezione con sirena e non stampa nulla
                self.msg_x_client = f"\nRicevuto il messaggio del: {self.data} con livello: {self.livello_acqua}|ATTIVA_SIRENA"
                print(
                    f"\nPERICOLO IN CORSO IN STAZIONE: {self.id_stazione}, nome del fiume: {nome_fiume}, località: {localita_fiume} misurazione effettuata il: {self.data}, lvl_misurato: {self.livello_acqua}"
                )
            else:
                self.msg_x_client = f"\nRicevuto il messaggio del: {self.data} con livello: {self.livello_acqua}|DISATTIVA_SIRENA"
                if self.livello_acqua >= lvl_guardia * 0.3:
                    # PERICOLO IMMINENTE
                    print(
                        f"\nPERICOLO IMMINENTE IN STAZIONE: {self.id_stazione}, nome del fiume: {nome_fiume}, località: {localita_fiume} misurazione effettuata il: {self.data}, lvl_misurato: {self.livello_acqua}"
                    )

            # non c'è un else perche il messaggio di default viene considerato sbagliato

    def kill(self):
        self.running = False


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, client_address = s.accept()  # bloccante
        print(f"il client {client_address} si è connesso")
        # per ogni client che si connette facci partire un thread (gestore client)
        thread = Client_handler(connection)
        thread.start()


if __name__ == "__main__":
    main()
