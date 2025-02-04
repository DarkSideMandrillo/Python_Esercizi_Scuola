import sqlite3
import socket
import threading

# Info generali del server
MY_ADDRESS = ("127.0.0.1", 9999)
BUFFER_SIZE = 4096


class Client_handler(threading.Thread):
    def __init__(self, connection, client_address):
        super().__init__()
        self.connection = connection
        self.client_address = client_address

    def run(self):
        try:
            with sqlite3.connect(
                "./fiumi.db"
            ) as conn:  # Mi apro il db, si chiude in automatico
                cur = conn.cursor()  # Mi creo il cursore che userò per navigare nel db

                while True:
                    message = self.connection.recv(
                        BUFFER_SIZE
                    ).decode()  # Prendo il messaggio e lo decripto
                    if len(message) == 3:
                        liv, id_stazione, data, ora = message.split(
                            "|"
                        )  # Mi prendo tutti i valori e dividendoli con la split
                        print(
                            f"Livello: {liv}, id_stazione: {id_stazione}, data: {data}, ora: {ora}"
                        )

                        query = f"""SELECT livello FROM livelli WHERE id_stazione = {id_stazione}"""  # Mi prendo tutti i livelli corrispondenti alla stazione dal db
                        cur.execute(query)  # Eseguisco la query
                        livelli_guardia = (
                            cur.fetchall()
                        )  # Mi prendo i livelli dal db della stazione del client

                        if (
                            livelli_guardia
                        ):  # Se ci sono dei livelli guardia ed il client ha inviato dati che sono presenti nel db

                            # Parte dei controlli, mi salvo già il messaggio che andrò ad inviare dopo al client
                            if liv < (livelli_guardia * 30 / 100):
                                response_client = "Avvenuta ricezione del messaggio"

                            elif liv >= (livelli_guardia * 30 / 100) and liv < (
                                livelli_guardia * 70 / 100
                            ):
                                response_client = "Avvenuta ricezione del messaggio"
                                query = f"""SELECT fiume, localita FROM livelli WHERE id_stazione = {id_stazione}"""  # Query che mi faccio per trovare il nome del fiume e della località x il messaggio al server
                                #!! basta fare una query sola
                                cur.execute(
                                    query
                                )  # Eseguo la query per prende i dati che mi mancano
                                fiume, localita = (
                                    cur.fetchall()
                                )  # Mi prendo fiume e localita

                                print(
                                    f"PERICOLO IMMINENTE! Livello ricevuto da {id_stazione} in data {data} e ora {ora}, in località {localita} che sorveglia il fiume {fiume}: {liv}"
                                )

                            elif liv >= (
                                livelli_guardia * 70 / 100
                            ):  #!! response_client non cambia mai dopo che si attiva una sirena
                                response_client = "Attivare la sirena!"
                                print(
                                    f"Pericolo in corso! Livello ricevuto da {id_stazione} in data {data} e ora {ora}, in località {localita} che sorveglia il fiume {fiume}: {liv}"
                                )
                        else:
                            response_client = (
                                "Campi non corretti o non presenti nel database"
                            )

                    else:
                        response_client = "Numero campi sbagliato"

                    self.connection.sendall(
                        response_client.encode()
                    )  # Mando il messaggio in base a in che if è entrato

        except Exception as e:
            print(f"Errore: {e}")
        finally:
            self.connection.close()
            print("Connessione chiusa col client")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()  # Aspetto che i client si connettano
    print("Server in ascolto wohoo")

    while True:
        connection, client_address = s.accept()  # Accetto la connessione di un client
        print(f"Connessione eseguita con {client_address}")
        client_handler = Client_handler(
            connection, client_address
        )  # Mi creo il thread per facilitare e far andare più veloce la procedura con + clienti
        client_handler.start()  # Starto il thread


if __name__ == "__main__":
    main()
