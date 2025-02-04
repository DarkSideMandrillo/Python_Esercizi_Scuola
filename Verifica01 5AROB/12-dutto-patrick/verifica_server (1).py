import sqlite3
import socket
import threading

# impostazioni server
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


# La classe per gestire le connessioni permettendo al server di gestire piu client contemporaneamente.
class nomeThread(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection  # connection: e la connessione socket che rappresenta il collegamento tra il server e un client.


def run(self):
    try:
        with sqlite3.connect("./fiumi.db") as conn_db:
            cur = (
                conn_db.cursor()
            )  # tramite questo cursore che si inviano comandi come SELEC.

            # controlla se ci sono messagi dal client
            while True:
                message = self.connection.recv(BUFFER_SIZE)
                if not message:
                    print("nessun messaggio ricevuto, chiusura connessione")
                    break

                query = 0

                tu = message.decode()  # varibile per fare lo split
                localitaf, livellof, oraf, dataf = tu.split(", ")

                if localitaf and livellof and oraf and dataf != None:  # primo controllo
                    query = f"""
                                SELECT 
                                FROM livelli 
                                WHERE localitaf == localita and livellof > ((livello%30)*100) 
                                """  #!! così è solo una stringa!!
                    messaggio = print("messagio e arrivato")
                    self.connection.sendall(messaggio.encode())

                elif (
                    localitaf and livellof and oraf and dataf != None
                ):  # secondo controllo
                    query = f"""
                                SELECT *
                                FROM livelli 
                                WHERE id = localita AND livellof >= ((livello%30)*100) AND ((livellof%70)*100) < livello
                                """
                    print("ALLERTA pericolo imminenete")
                    messaggio = print("messaggio e arrivato")
                    self.connection.sendall(messaggio.encode())

                elif (
                    localitaf and livellof and oraf and dataf != None
                ):  # terzo controllo
                    query = f"""
                                SELECT 
                                FROM livelli 
                                WHERE localitaf == localita and livellof > ((livello%70)*100)
                                """
                    print("ALLERTA: livello dell acqua troppo alto")
                    messaggio = print(
                        "livello troppo alto accendere la sirena luminosa"
                    )
                    #!! dividi i print dall'assegnazione
                    self.connection.sendall(messaggio.encode())

                    # Viene eseguita quando il messaggio ricevuto dal client non corrisponde a nessuna delle azioni previste
                else:
                    self.connection.sendall(
                        "Errore ricezione o input scorretti".encode()
                    )
                    continue

    except (
        Exception
    ) as e:  # as e: assegna l'oggetto dell'eccezione a una variabile (e), in modo che sia possibile accedere al messaggio o ai dettagli dell'errore.
        print(
            f"Errore: {e}"
        )  # Il testo "Errore: " e seguito dal messaggio dell'eccezione memorizzato in e.

    finally:  # chiude la conessione una volta terminato
        self.connection.close()
        print("Connessione chiusa con il client")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, client_address = s.accept()
        print(f"Il client {client_address} si e connesso")
        thread = nomeThread(connection)
        thread.start()  # avvia il thread, il quale eseguira il metodo run() definito nella classe.


if __name__ == "__main__":
    main()
