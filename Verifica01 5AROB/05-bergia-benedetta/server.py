import sqlite3
import threading
import socket

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


class Client(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        id_stazione = self.connection.recv(
            BUFFER_SIZE
        ).decode()  # ricevo id una volta sola
        self.connection.sendall(
            "ricevuta stazione".encode()
        )  #!! Per come era scritta la consegna l'ID sarebbe dovuto essere inviato ogni volta
        while True:
            conn = sqlite3.connect(
                "fiumi.db", check_same_thread=False
            )  #!! Connetti ogni volta ma non chiudi mai!
            cur = conn.cursor()
            message = self.connection.recv(BUFFER_SIZE).decode()
            livello, data, ora = message.split("|")
            # print(id_stazione)
            # print(livello, data, ora, id_stazione)
            queryLivello = f"""SELECT livello
            FROM livelli
            WHERE id_stazione = {id_stazione}"""  #!! ? SELECT*
            queryNome = f"""SELECT fiume
            FROM livelli
            WHERE id_stazione = {id_stazione}"""
            queryLocalita = f"""SELECT localita
            FROM livelli
            WHERE id_stazione = {id_stazione}"""
            cur.execute(queryLivello)
            conn.commit()
            risposta = cur.fetchall()
            livello_tabella = float(risposta[0][0])
            livello = float(livello)
            cur.execute(queryNome)
            conn.commit()
            risposta = cur.fetchall()
            nome = risposta[0][0]
            cur.execute(queryLocalita)
            conn.commit()
            risposta = cur.fetchall()
            localita = risposta[0][0]

            print(f"ricevuto: {nome}, {localita}, {data}, {ora}")
            if livello < (livello_tabella * 0.3):
                # print("<30%")
                self.connection.sendall("avvenuta ricezione".encode())
            elif livello >= (livello_tabella * 0.3) and livello < (
                livello_tabella * 0.7
            ):
                # print(">=30%   <70%")
                print("-> PERICOLO IMMINENTE")
                self.connection.sendall("avvenuta ricezione".encode())
            else:
                # print(">70%")
                print("-> PERICOLO IN CORSO")
                self.connection.sendall("ATTIVARE SIRENA".encode())


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, ip_address = s.accept()
        print(f"connesso host: {ip_address}")
        thread = Client(connection)
        thread.start()


if __name__ == "__main__":
    main()
