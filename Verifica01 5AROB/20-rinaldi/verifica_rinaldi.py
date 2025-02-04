import socket
import threading
import sqlite3

# thread_list = []

ip_address = ("127.0.0.1", 8080)


class nomeThread(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):  #!! ma un ciclo in tutto questo?
        print(f"connesso a {self.connection[1]}")
        try:
            msg = self.connection[0].recv(4096).decode()
            print(msg)
            """
                Il messaggio arriverà come 
                Identificativo|livello|data&ora
            """

            id, livello, data = msg.split("|")

            livello = float(livello)

            conn = sqlite3.connect("fiumi.db", check_same_thread=False)
            cur = conn.cursor()
            cur.execute(
                f"""SELECT *
                        FROM livelli
                        Where id_stazione = {id}"""
            )
            conn.commit()
            res = cur.fetchall()
            conn.close()
            if not res:
                self.connection[0].sendall("Non esisti nel DB".encode())
            else:
                self.connection[0].sendall("Corretto".encode())
        except Exception as e:
            print(f"Errore {e}")
            self.connection[0].sendall("Errore riprova".encode())

        """
            Ora controllo i dati e agisco di conseguenza
        """

        conn = sqlite3.connect("fiumi.db", check_same_thread=False)
        cur = conn.cursor()
        cur.execute(
            f"""SELECT *
                        FROM livelli
                        Where id_stazione = {id}"""
        )
        conn.commit()
        res = cur.fetchall()
        conn.close()

        # print(res.split())

        identificativo, fiume, localita, guardia = str(res).split(",")

        lista = guardia.split(")")

        guardia = float(lista[0])

        if livello * 30 / 100 < guardia:
            self.connection[0].sendall("ricevuto".encode())
        elif (
            livello * (30 / 100) >= guardia and livello * (30 / 100) < guardia
        ):  #!! sempre 30?
            self.connection[0].sendall("ricevuto".encode())
            print(
                f"Pericolo imminente livello:{livello}\nFiume: {fiume}\nLocalità: {localita}\ndata: {data}\n"
            )
        elif livello * (70 / 100) >= guardia:
            self.connection[0].sendall("Pericolo".encode())
            print(
                f"Pericolo in corso livello:{livello}\nFiume: {fiume}\nLocalità: {localita}\ndata: {data}\n"
            )


if __name__ == "__main__":

    print("start")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ip_address)
    server.listen()
    while True:
        connection = server.accept()

        thread = nomeThread(connection)
        thread.start()
        # thread_list.append(thread)
