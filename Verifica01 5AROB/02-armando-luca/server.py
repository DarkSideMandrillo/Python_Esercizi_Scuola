import socket
import threading
import sqlite3

MY_ADDRESS = ("127.0.0.1", 8000)
BUFFER_SIZE = 4096


class Client_Handler(threading.Thread):
    def __init__(self, connection, client_address):
        super().__init__()
        self.connection = connection
        self.client_address = client_address

    def run(self):
        print(f"connessione al client {self.client_address}")

        conn_db = sqlite3.connect("fiumi.db")  # connessione al db
        cursor = conn_db.cursor()

        while True:
            ricevuto = self.connection.recv(
                BUFFER_SIZE
            ).decode()  # ricevo messaggio dal client

            messaggio = ricevuto.split("|")  # lista variabili messaggio ricevuto
            # print(messaggio)
            livello = float(
                messaggio[0]
            )  # assegnazione in variabili del messaggio ricevuto
            data_ora = messaggio[1]
            id = messaggio[2]

            stringa = f"SELECT fiume, localita, livello FROM livelli WHERE id_stazione = {id}"  # query per informazioni della stazione con l'id ricevuto
            cursor.execute(stringa)
            informazioni = cursor.fetchall()[
                0
            ]  # [0] perche restituisce tupla di liste e prendo solo la prima lista
            # print(informazioni)
            fiume = informazioni[
                0
            ]  # assegnazione in variabili delle informazioni della stazione con id ricevuto
            localita = informazioni[1]
            livello_guardia = float(
                informazioni[2]
            )  # float perchè se no con str non posso fare il confronto
            risposta = ""
            if (
                livello < livello_guardia / 30 * 100
            ):  # controllo il livello e invio risposta
                risposta = "livello ricevuto"

            elif (
                livello >= livello_guardia / 30 * 100
                and livello < livello_guardia / 70 * 100
            ):
                risposta = "livello ricevuto"
                print(
                    f"pericolo imminente fiume: {fiume}, localita: {localita}, data e ora: {data_ora}"
                )

            elif livello_guardia / 70 * 100:
                risposta = "attiva sirena"
                print(
                    f"pericolo in corso fiume: {fiume}, localita: {localita}, data e ora: {data_ora}"
                )

            self.connection.sendall(risposta.encode())

        #!! Manca il try:
        conn_db.close()  # chiude connessione con il db
        self.connection.close()  # chiude connesione con il client
        print(f"connessione chiusa con {self.client_address}")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creo il socket
    s.bind(MY_ADDRESS)
    s.listen()
    print("server in attesa di connesioni")

    while True:
        connection, client_address = s.accept()
        client_handler = Client_Handler(
            connection, client_address
        )  # creo il thread per gestire la connesione di più client insieme
        client_handler.start()  # faccio partire il thread


if __name__ == "__main__":
    main()
