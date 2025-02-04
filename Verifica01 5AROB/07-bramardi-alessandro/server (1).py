import threading
import sqlite3
import socket

MYADDRESS = ("127.0.0.1", 9080)
BUFFERSIZE = 4096


class client_handler(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        db = sqlite3.connect("fiumi.db")
        cur = sqlite3.Cursor(db)  #!!  cur = db.cursor()
        with self.conn:
            while True:
                request = self.conn.recv(BUFFERSIZE)
                if not request:
                    break
                request = request.decode()
                response = self.give_response(cur, request)
                self.conn.sendall(response.encode())
        db.close()
        self.conn.close()

    def give_response(self, cur, request):
        mex = request.split(":")
        # print(mex)
        date = mex[0]
        livello = float(mex[1])
        stazione = mex[2]
        variabili = self.get_valori(stazione, cur)
        livello_staz = variabili[0]
        fiume = variabili[1]
        localita = variabili[2]

        if livello < (livello_staz / 100) * 30:
            print(
                f"Analisi livello in data: {date}, sul fiume {fiume} presso{localita}"
            )
            return "Messaggio ricevuto correttamente"
        elif (
            livello >= (livello_staz / 100) * 30 and livello < (livello_staz / 100) * 70
        ):
            print(
                f"Analisi livello in data: {date}, sul fiume {fiume} presso{localita}"
            )
            print("Pericolo imminente")
            return "Messaggio ricevuto correttamente"
        elif livello >= (livello_staz / 100) * 70:
            print(
                f"Analisi livello in data: {date}, sul fiume {fiume} presso{localita}"
            )
            print("Pericolo in corso")
            return "Attivazione sirena richiesta"

    def get_valori(self, stazione, cur):
        query = f"SELECT livelli.livello, livelli.fiume, livelli.localita FROM livelli WHERE livelli.id_stazione = '{stazione}'"
        cur.execute(query)
        valori = cur.fetchone()
        # print(valori)
        return valori


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(MYADDRESS)
    server.listen()
    while True:
        conn, addr = server.accept()
        print(f"Il client {addr} si è connesso")
        stazione = client_handler(conn, addr)
        stazione.start()


if __name__ == "__main__":
    main()
