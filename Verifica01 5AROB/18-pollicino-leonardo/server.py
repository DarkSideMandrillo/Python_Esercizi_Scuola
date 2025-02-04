import datetime  #!! non usato
import socket
import threading
import sqlite3
import time  #!! non usato

INDIRIZZO = ("localhost", 9090)
BUFFER_SIZE = 4096


class client_handler(threading.Thread):
    def __init__(self, connessione):
        super().__init__()
        self.connessione = connessione
        self.conn = sqlite3.connect("fiumi.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.query = False

    def run(self):
        while True:
            dati = self.connessione.recv(BUFFER_SIZE)
            if not dati:
                print("connessione chiusa dal client")
                break
            dati = dati.decode()
            # print(dati)
            liv_acqua, data, stazione = dati.split("|")
            liv_acqua = float(liv_acqua)
            # print(liv_acqua, data, stazione)
            # self.connessione.sendall(dati.encode())
            if not self.query:
                self.cur.execute(
                    "SELECT * FROM livelli WHERE id_stazione = ?", (stazione,)
                )
                var = self.cur.fetchall()
                self.query = True
                self.conn.close()  #!! ? chiusura connessione db? Capisco l'intento, ma il DB potrebbe cambiare in tempo reale, in questo casi bisognerebbe riavviare tutti i client
            # print(var)
            if len(var) > 0:
                _, fiume, localita, liv_guardia = var[0]
                # print(fiume, localita, liv_guardia)
                if liv_acqua < (liv_guardia / 100 * 30):
                    self.connessione.sendall("Ricevuta misurazione".encode())
                elif liv_acqua < (liv_guardia / 100 * 70):
                    self.connessione.sendall("Ricevuta misurazione".encode())
                    print(
                        f"pericolo imminente per stazione {stazione}\nFiume: {fiume} località: {localita} Data: {data}"
                    )
                elif liv_acqua >= (liv_guardia / 100 * 70):
                    self.connessione.sendall("Attiva sirena luminosa".encode())
                    print(
                        f"pericolo in corso per stazione {stazione}\nFiume: {fiume} località: {localita} Data: {data}"
                    )
                else:
                    self.connessione.sendall("caso non previsto".encode())
            else:
                self.connessione.sendall("Stazione errata".encode())
                break
        self.conn.close()
        self.connessione.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(INDIRIZZO)
    s.listen()
    while True:
        connessione, client_address = s.accept()
        print(f"{client_address} si è connesso")
        thread = client_handler(connessione)
        thread.start()


if __name__ == "__main__":
    main()
