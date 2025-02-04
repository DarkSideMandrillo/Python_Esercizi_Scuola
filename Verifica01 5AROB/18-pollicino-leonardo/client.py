import socket
import datetime
import time
import random

INDIRIZZO_SERVER = ("localhost", 9090)
BUFFER_SIZE = 4096
TEMPO = 3
livello_fiume = 4


def accendi_sirena():
    print("Sirena luminosa accesa")


def spegni_sirena():
    print("Sirena luminosa spenta")


def main():
    sirena_accesa = False
    ident = int(input("inserisci l'identificativo della stazione: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(INDIRIZZO_SERVER)
    while True:
        livello_fiume = random.randint(0, 15)
        invia = f"{livello_fiume}|{datetime.datetime.now()}|{ident}"
        print(invia)
        s.sendall(invia.encode())
        messaggio = s.recv(BUFFER_SIZE)
        messaggio = messaggio.decode()
        print(messaggio)
        if messaggio == "Stazione errata":
            break
        if messaggio == "Attiva sirena luminosa":
            if not sirena_accesa:
                accendi_sirena()
                sirena_accesa = True
        else:
            if sirena_accesa:
                spegni_sirena()
                sirena_accesa = False
        time.sleep(TEMPO)
    s.close()


if __name__ == "__main__":
    main()
