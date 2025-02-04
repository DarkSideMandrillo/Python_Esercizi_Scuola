import socket
import threading
import sqlite3

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096


class serverThread(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        while True:
            messageClient = self.connection.recv(
                BUFFER_SIZE
            )  # ricezione del messaggio da client
            messageClient = messageClient.decode()
            infoClient = messageClient.split("|")
            with sqlite3.connect(
                "fiumi.db"
            ) as conn:  # apertura connessione con database
                cur = conn.cursor()  #!! apri a ogni messaggio
                cur.execute(
                    f"""SELECT * 
                                FROM livelli
                                WHERE id_stazione = {infoClient[0]}
                            """
                )
                conn.commit()
                risultato = (
                    cur.fetchall()
                )  # acquisizione risultato dall'interrogazione query
                # print(risultato[0][3] / 100 * 30)
                # print(risultato[0][3] / 100 * 70)
                livelloClient = float(infoClient[1])
                livello1 = float(risultato[0][3]) / 100 * 30  #!! un poco ridondante
                livello2 = float(risultato[0][3]) / 100 * 70
                print(f"{risultato[0][1]} | {risultato[0][2]} | {infoClient[2]}")
                if livelloClient > livello1:  # gestione primo caso
                    self.connection.sendall("Messaggio ricevuto".encode())
                if (
                    livelloClient >= livello1 and livelloClient < livello2
                ):  # gestione secondo caso
                    self.connection.sendall("Messaggio ricevuto".encode())
                    print("Pericolo imminente")
                if livelloClient >= livello2:  # gestione terzo caso
                    self.connection.sendall("Allarme".encode())
                    print("PERICOLO")


def main():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )  # attivazione socket
    server_socket.bind(MY_ADDRESS)  # assegnazione dell'ip
    server_socket.listen()  # server in attesa di connessioni

    while True:
        connessione, indirizzo_client = (
            server_socket.accept()
        )  # attivazione connessione con client
        # print(f"Client {indirizzo_client} connesso.")

        thread_client = serverThread(
            connessione
        )  # attivazione di più thread per gestire multi-client
        thread_client.start()


if __name__ == "__main__":
    main()
