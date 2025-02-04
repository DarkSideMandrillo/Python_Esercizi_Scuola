import socket
import threading
import sqlite3

MYADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


class serverThread(threading.Thread):
    def __init__(self, connection, address, id):
        super().__init__()
        self.connection = connection
        self.address = address
        self.livello = None
        self.data = None
        self.id = id
        self.livelloDb = None
        self.fiumeDb = None
        self.localitaDb = None
        self.idDb = None

    def riceviMisurazione(self):
        messaggio = self.connection.recv(BUFFER_SIZE).decode()
        messaggioSplit = messaggio.split("|")
        if messaggio:
            return messaggioSplit[0], messaggioSplit[1]
        else:
            return None, None

    def readDb(self, nomeFile):  #!! apro per ogni comunicazione
        with sqlite3.connect(nomeFile) as conn:
            c = conn.cursor()
            query = "SELECT * FROM livelli WHERE id_stazione=?"
            c.execute(query, (self.id))
            listaDb = c.fetchall()
            tuplaDb = listaDb[0]
            print(tuplaDb)
            return tuplaDb[0], tuplaDb[1], tuplaDb[2], tuplaDb[3]

    def calcolaCasistiche(self):
        trenta = self.livelloDb * 30 / 100
        settanta = self.livelloDb * 70 / 100
        if int(self.livello) < trenta:
            self.connection.sendall(f"avvenuta ricezione".encode())
        elif int(self.livello) >= trenta and int(self.livello) < settanta:
            self.connection.sendall(f"avvenuta ricezione".encode())
            print("pericolo imminente")
        elif int(self.livello) >= settanta:
            self.connection.sendall(f"richiesta attivazione sirena luminosa".encode())
            print("pericolo")
        print(
            f"il fiume: {self.fiumeDb}, situato in localita: {self.localitaDb}, ha misurato il giorno: {self.data}"
        )

    def calcolaRisposta(self):
        self.idDb, self.fiumeDb, self.localitaDb, self.livelloDb = self.readDb(
            "fiumi.db"
        )
        self.calcolaCasistiche()

    def run(self):
        while self.connection:
            self.livello, self.data = self.riceviMisurazione()
            if self.livello:
                self.calcolaRisposta()
            else:
                break
        print(f"connessione chiusa per il client{self.address}")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MYADDRESS)
    s.listen()
    print("Server in ascolto...")

    while True:
        connessione, clientAddress = s.accept()
        print(f"Il client {clientAddress} si è connesso")
        id = connessione.recv(BUFFER_SIZE).decode()
        threadClient = serverThread(connessione, clientAddress, id)
        threadClient.start()


if __name__ == "__main__":
    main()
