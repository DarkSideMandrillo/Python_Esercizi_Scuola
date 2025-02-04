import socket
import threading
import time
import datetime
import random

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

"""
FORMATO MSG = lvl_misurato|data&ora|id_stazione
"""


class Stazione(threading.Thread):
    def __init__(self, s, latenza, id_stazione):
        super().__init__()
        self.s = s
        self.running = True
        self.id_staz = id_stazione
        self.altezza_lvl = None
        self.latenza = latenza
        self.sirena_accesa = False

    def run(self):

        while self.running:
            self.altezza_lvl = float(random.randint(0, 10))
            data_ora = datetime.datetime.now()
            print(f"data e ora: {data_ora}")
            self.s.sendall(f"{self.altezza_lvl}|{data_ora}|{self.id_staz}".encode())
            message = self.s.recv(BUFFER_SIZE)
            print(f"risposta da server: {message.decode()}")
            # in base alla risposta capisce de accendere sirena
            if message.decode().split("|")[1] == "ATTIVA_SIRENA":
                self.sirena_accesa = True
                print("SIRENA ACCESA")
            else:
                self.sirena_accesa = False
                print("SIRENA SPENTA")
            # aspetta il tempo di latenza tra una misurazione e l'altra
            time.sleep(self.latenza)

    def kill(self):
        self.running = False


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    # s.sendall(f'PRESENTO'.encode())

    latenza = int(input("inserisci la latenza di ogni misurazione (in secondi): "))
    id_stazione = int(input("inserisci l'id della stazione: "))
    thread = Stazione(
        s, latenza, id_stazione
    )  #!! bello tutto, ma perchè la stazione dovrebbe essere un thread?
    thread.start()


if __name__ == "__main__":
    main()
