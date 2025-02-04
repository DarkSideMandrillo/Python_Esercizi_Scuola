import socket
import time
import datetime
import random

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    print("inserisci il tempo di attesa")
    attesa = int(input("->"))
    print("inserisci l'id della stazione")
    id = int(input("->"))
    s.sendall(f"{id}".encode())
    while True:
        livello = random.randint(0, 20)
        data = datetime.datetime.now()
        print(f"data:{data}")
        s.sendall(f"{livello}|{data}".encode())
        risposta = s.recv(BUFFER_SIZE).decode()
        if risposta == "preicolo":
            print("attivazione sirena")
        else:
            print(risposta)
        time.sleep(attesa)


if __name__ == "__main__":
    main()
