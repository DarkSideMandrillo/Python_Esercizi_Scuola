import sqlite3
import socket
import threading


INDIRIZZO_SERVER = ("localhost", 7777)
BUFFER = 4096

class client_heandler(threading.Thread):
    def __init__(self, connessione):
        super().__init__()
        self.connessione = connessione

    def run(self):
        try:
            with sqlite3.connect("fiumi.db") as connessione_db:
                cur = connessione_db.cursor()
                ##sirena = False
                
                while True:
                    #ricevo i messaggi dal client
                    messaggio = self.connessione.recv(BUFFER).decode()

                    print(f"INFO ORARIO/DATA: {messaggio}")
                    id_stazione, livello_misurato, data_e_ora = messaggio.split(";")
                    livello_misurato = float(livello_misurato)

                    #eseguo la query scritta e salvo le informazioni in informazioni
                    cur.execute("""SELECT fiume, localita, livello FROM livelli WHERE id_stazione = ?""", (id_stazione,))
                    informazioni = cur.fetchone()

                    if informazioni:
                        fiume, localita, livello_guardia = informazioni

                        #se il livello è sotto il 30% del livello di guardia
                        if (livello_misurato < (0.3 * livello_guardia)):
                            self.connessione.sendall("MESSAGGIO RICEVUTO".encode())

                        #se il livello è tra 30% e 70% del livello de guardia
                        elif (0.3 * livello_guardia <= livello_misurato < 0.7 * livello_guardia):       
                            self.connessione.sendall("MESSAGGIO RICEEVUTP".encode())
                            print(f"PERICOLO A {localita}")
                        
                        #se il livello è sopra o uguale al 70%
                        else:
                            self.connessione.sendall("richiesta attivazione sirena".encode())
                            print(f"ATTIVAZIONE SIRENA A {localita}")
                    else:
                        self.connessione.sendall("ricerca stazione con esito NEGATIVO".encode())
        finally:
            self.connessione.close()


def main():
    #socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(INDIRIZZO_SERVER)
    server_socket.listen()

    while True:
        connessione, indirizzo_client = server_socket.accept()
        print(f"client: {indirizzo_client}")
        thread = client_heandler(connessione)
        thread.start()


if __name__ == "__main__":
    main()