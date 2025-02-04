"""
casistiche delle risposte:
 ● nel caso in cui il livello misurato sia inferiore al 30% del livello di guardia esso invia un
 messaggio di avvenuta ricezione al client e non stampa nulla sulla console del server;
    "0|dati ricevuti"
 ● nel caso in cui il livello misurato sia maggiore o uguale al 30% del livello di guardia e minore
 del 70%, esso invia un messaggio di avvenuta ricezione al client e stampa un avviso di
 pericolo imminente sulla console del server;
    "0|dati ricevuti"
 ● nel caso in cui il livello misurato sia maggiore o uguale al 70% del livello di guardia esso
 invia un messaggio al client che richieda l’attivazione della sirena luminosa e stampa un
 avviso di pericolo in corso sulla console del server.
    "1|accensione sirena"
    
0 --> sirena spenta situazione non di pericolo in corso
1 --> sirena accesa situazione di pericolo in corso
"""

import socket

import socket
import threading
import sqlite3

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True

    def run(
        self,
    ):  # apro il db e prendo i dati dal db della stazione a cui è connesso il thread
        conn = sqlite3.connect("fiumi.db")
        cur = conn.cursor()
        while self.running:
            msg = self.connection.recv(BUFFER_SIZE)
            msg = msg.decode().split(
                "|"
            )  # splitto il messaggio per dividere i dati inviati dal client
            misurazione = float(msg[0])
            data = msg[1]
            ora = msg[2]
            id = msg[3]
            # prendo i dati dal db
            cur.execute(
                f""" SELECT fiume, localita, livello
                            FROM livelli
                            WHERE id_stazione = {id}
                        """
            )
            conn.commit()
            datiDB = cur.fetchall()
            fiume = datiDB[0][0]
            localita = datiDB[0][1]
            livello = float(datiDB[0][2])
            # controllo le casistiche
            if misurazione < ((livello * 30) / 100):
                self.connection.sendall("0|dati ricevuti".encode())
                print(
                    f"dati del {data} ricevuti alle ore {ora} dalla stazione di {localita} che controlla il fiume {fiume}"
                )
            elif misurazione >= ((livello * 30) / 100) and misurazione < (
                (livello * 70) / 100
            ):
                self.connection.sendall("0|dati ricevuti".encode())
                print("\t\tATTENZIONE\n\t  PERICOLO IMMINENTE")
                print(
                    f"dati del {data} ricevuti alle ore {ora} dalla stazione di {localita} che controlla il fiume {fiume}"
                )
            elif misurazione >= ((livello * 70) / 100):
                self.connection.sendall("1|accensione_sirena()".encode())
                print("\t\tATTENZIONE\n\t  PERICOLO IN CORSO")
                print(
                    f"dati del {data} ricevuti alle ore {ora} dalla stazione di {localita} che controlla il fiume {fiume}"
                )

    def kill(self):
        self.running = False
        self.connection.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()  #!! piu di 5 connessioni
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()


if __name__ == "__main__":
    main()
