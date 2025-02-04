import socket
import time
import datetime

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    while True:  #!! da migliorare, ma corretto

        attesa = 15  # secondi
        idStazione = 1
        livello = 10
        date = datetime.datetime.now()  # acquisizione dell'ora in tempo reale

        message = f"{idStazione}|{livello}|{date}"
        s.sendall(message.encode())  # invio del messaggio al server
        rispostaServer = s.recv(BUFFER_SIZE)  # ricezione del messaggio
        rispostaServer = rispostaServer.decode()
        if str(rispostaServer) == "Allarme":  # gestione 3 caso
            print("Attivazione della sirena luminosa")
        else:
            print(rispostaServer)
        time.sleep(attesa)

    s.close()


if __name__ == "__main__":
    main()
