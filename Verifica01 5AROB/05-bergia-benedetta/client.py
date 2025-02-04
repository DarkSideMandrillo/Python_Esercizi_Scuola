import socket
import time
import datetime
import random

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect(SERVER_ADDRESS)  #!! Perchè usare conn?
    # tempo = input("inserire tempo: ")
    tempo = 10  # tempo di attesa

    # prendo data e ora
    data_tempo = datetime.datetime.now()  #!! nel while!
    data, ora = str(data_tempo).split(" ")
    ora = str(ora).split(".")[0]
    print(data, ora)

    # invio id stazione una volta sola
    stazione = "5"
    s.sendall(stazione.encode())
    message = s.recv(BUFFER_SIZE).decode()
    print(message)
    while True:
        livello = random.randint(1, 10)
        message = f"{livello}|{data}|{ora}"
        print(f"ho inviato {message}")
        # messaggio = "livello|data|ora|id_stazione"
        s.sendall(message.encode())
        message = s.recv(BUFFER_SIZE).decode()
        print(message)
        time.sleep(tempo)


if __name__ == "__main__":
    main()
