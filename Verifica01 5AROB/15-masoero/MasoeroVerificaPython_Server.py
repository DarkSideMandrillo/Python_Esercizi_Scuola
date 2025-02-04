import socket
import threading
import sqlite3

# indirizzo e porta del server oltre alla dimensione massima del buffer
MY_ADDRESS = ("0.0.0.0", 9090)
BUFFER_SIZE = 4096


# definisco la classe per gestire ogni thread e ogni classe correlata
class client_handler(threading.Thread):
    def _init_(self, connection):  #!! errore sintassi
        super()._init_()
        self.connection = connection
        # tramite la funzione seguente mi connetto al database
        self.conndb = sqlite3.connect("fiumi.db", check_same_thread=False)
        # con la funzione cur posso operare sul database tramite comandi
        self.cur = self.conndb.cursor()

    # avvio il thread e di conseguenza tutte le sue funzioni
    def run(self):
        while True:
            # mi metto in ricezione dei dati inviati dal client
            # dimensione massima BUFFER_SIZE
            comando = self.connection.recv(BUFFER_SIZE)
            if not comando:
                print("Il client ha chiuso la connessione.")
                self.conndb.close()
                self.connection.close()
                break
            # essendo il comando un messaggio codificato, lo decodifico
            comando = comando.decode()
            print(comando)
            # se il messaggio equivale a exit
            # termino la comunicazione
            if comando == "exit":
                self.connection.sendall("comunicazione terminata".encode())
                self.close()  ##!! cosa chiudi?
                break
            # se è presente la pipe nel messaggio allora devo splittarlo
            # ottengo così tutti i campi necessari
            elif "|" in comando:
                vet = comando.split("|")
                # verifico il numero dei campi
                # per eventualmente gestire protocolli differenti da più o meno campi
                if len(vet) == 4:
                    richiesta, livello, dataOra, idStazione = vet
                    # verifico la tipologia di richiesta
                    if richiesta == "verificaLivello":
                        # tramite la query SQL ottengo la soglia di guardia del fiume
                        # lavoro in base all'ID della stazione
                        self.cur.execute(
                            "SELECT livello FROM livelli WHERE id_stazione = ?",
                            (idStazione),
                        )
                        var = self.cur.fetchall()
                        print(var)  #!! var è una lista di tuple
                        # confronto il livelllo del fiume in relazione alla guardia
                        # definisco il grado di pericolo
                        if (
                            livello >= (var * 0.3) + var and livello < (var * 0.7) + var
                        ):  #!! livello deve essere trasformato in float
                            self.connection.sendall(
                                f"Messaggio Ricevuto {dataOra}".encode()
                            )

                            self.cur.execute("SELECT fiume FROM livelli")  #!! select *
                            fiume = self.cur.fetchall()
                            self.cur.execute("SELECT localita FROM livelli")
                            localita = self.cur.fetchall()
                            # dopo aver ricavato il nome e la localita tramite query
                            # li stampo nella console del server
                            print(f"{fiume}|{localita}|{var} Pericolo Imminente")

                        elif livello >= (var * 0.7) + var:
                            self.connection.sendall(
                                f"{var} DANGER, attivazione sirena luminosa".encode()
                            )

                            self.cur.execute(
                                "SELECT fiume FROM livelli WHERE id_stazione = ?",
                                (idStazione),
                            )
                            fiume = self.cur.fetchall()
                            self.cur.execute(
                                "SELECT localita FROM livelli WHERE id_stazione = ?",
                                (idStazione),
                            )
                            localita = self.cur.fetchall()
                            # dopo aver ricavato il nome e la localita tramite query
                            # li stampo nella console del server
                            print(f"{fiume}|{localita}|{var} PERICOLO IN CORSO")

                        else:
                            # se il livello è inferiore al 30% non c'è pericolo
                            self.connection.sendall(
                                f"{dataOra} Avvenuta Ricezione".encode()
                            )
                    else:
                        # non avendo altre tipologie di richieste gestisco in questa maniera
                        self.connection.sendall(
                            f"{comando} non è presente nella lista di comandi".encode()
                        )
                else:
                    # non avendo altr protocolli di comunicazione gestisco in questa maniera
                    self.connection.sendall(
                        f"{comando} non è presente nella lista di comandi".encode()
                    )
            else:
                # non accettando messaggi senza pipe a parte exit gestisco in questa maniera
                self.connection.sendall(
                    f"{comando} non è presente nella lista di comandi".encode()
                )


def main():
    # creo un socket e associo gli indirizzi alle porte
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        # in attesa di connessione
        connection, client_address = s.accept()
        print(f"Il client {client_address} si è connesso")
        # ad ogni nuovo client che si collega, si avvia un nuovo thread
        thread = client_handler(connection)
        thread.start()


if __name__ == "__main__":
    main()
