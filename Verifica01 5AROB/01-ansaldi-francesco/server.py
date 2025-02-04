import socket
import threading
import sqlite3

SERVER_ADDRESS = ("127.0.0.1", 12345)
BUFFERSIZE = 4096


class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address):
        super().__init__()  # inizializza il thread.
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        # gestisce la comunicazione con il client.
        print(f"Connessione da {self.client_address}")
        try:
            data = self.client_socket.recv(
                BUFFERSIZE
            ).decode()  # Riceve dati dal client e li decodifica.
            print(f"Ricevuto dal client {self.client_address}: {data}")

            response = self.process_request(data)
            self.client_socket.send(
                response.encode()
            )  # Codifica e invia la risposta al client.
        finally:
            self.client_socket.close()  # Chiude la connessione con il client.
            print(f"Connessione chiusa con {self.client_address}")

    def process_request(self, data):
        conn = sqlite3.connect("fiumi.db")  # connessione con il db #!! Apri ogni volta
        cursor = conn.cursor()  # per eseguire comandi SQL

        livelli = data.split(",")
        localita = livelli[0]
        livello = livelli[1]  #!! Da convertire a float
        data_segn = livelli[2]

        cursor.execute(
            "SELECT livello FROM livelli WHERE localita = ?", (localita,)
        )  #!! Possono esserci 2 localita uguali
        result = cursor.fetchone()  # Recupera il risultato

        if result:  #!! Result è una lista di tuple
            if livello > result:
                trent_perc = result * 30 / 100
                sett_perc = result * 70 / 100
                if livello >= result + trent_perc:
                    response = f"localita '{localita}' ricevuta: Livello= {livello} Data= {data_segn}"
                    print("Percolo imminente!!!")
                elif livello >= result + sett_perc:
                    response = f"richiesta attivazione sirena"
                    print("Percolo in corso")
            elif livello <= result:
                if livello > result - trent_perc:
                    response = f"localita '{localita}' ricevuta: Livello= {livello} Data= {data_segn}"
                if livello < result - sett_perc:
                    response = f"localita '{localita}' ricevuta: Livello= {livello} Data= {data_segn}"
                    print("Percolo imminente!!!")
        else:
            response = f"localita '{localita}' non trovata."

        conn.close()  # Chiude la connessione al database
        return response


def start_server():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )  # creo un socket TCP.
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(
        5
    )  # imposto il socket per ascoltare fino a 5 connessioni. #!! Ma le possibili conn sono 10
    print(f"Server in ascolto su {SERVER_ADDRESS}")

    while True:
        client_socket, client_address = (
            server_socket.accept()
        )  # accetto una connessione.
        client_handler = ClientHandler(
            client_socket, client_address
        )  # creo un handler per il client.
        client_handler.start()


if __name__ == "__main__":
    start_server()
