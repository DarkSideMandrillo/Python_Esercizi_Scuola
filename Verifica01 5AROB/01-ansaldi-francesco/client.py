import socket
import datetime
import random
import time

SERVER_ADDRESS = ("127.0.0.1", 12345)
BUFFERSIZE = 4096


def attivazione_sirena():
    print("Sirena luminosa accesa ")


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)
    localita = input("Inserisci il nome della localita: ")

    while True:  # Inizia un ciclo infinito per mantenere il client attivo fino a uscita
        data = datetime.datetime.now()
        livello = random.choice(range(0.0, 25.0))  ##!! Errore
        message = f"{localita},{livello},{data}"
        client_socket.send(
            message.encode()
        )  # codifica il messaggioe lo invia al server

        response = client_socket.recv(
            BUFFERSIZE
        ).decode()  # riceve la risposta dal server e decodifica in stringa
        print(f"Risposta del server: {response}")
        if response == "richiesta attivazione sirena":
            attivazione_sirena()
        time.sleep(15)


if __name__ == "__main__":
    start_client()  # Avvia la funzione principale del client
