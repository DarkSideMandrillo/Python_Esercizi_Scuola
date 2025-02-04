import socket, datetime, time

BUF_SIZE = 4096  # buffer size per la recv
SERVER_ADDRESS = ("127.0.0.1", 9090)  # indirizzo a cui il client si deve collegare
FREQUENZA_MESSAGGIO = 15  # ogni quanto vengono richiesti gli input


class Sirena:
    # La classe sirena serve per la gestione della stampa della sirena accesa
    def __init__(self) -> None:
        pass

    def up(self):  # attiva la sirena
        print("ACCENDO LA SIRENA")

    def down(self):  # spegni la sirena
        print("SPENGO LA SIRENA")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    sirena = Sirena()

    while True:
        # input che si manderanno al server:
        id_stazione = int(
            input("inserisci l'identificativo della stazione: ")
        )  #!! la stazione non cambia a ogni messaggio
        livello_misurato = float(input("inserisci il livello misurato del fiume: "))
        data = datetime.datetime.now()
        # mando il messaggio formattato nel seguente modo, successivamente nel server faccio la split
        s.sendall(f"{id_stazione}|{livello_misurato}|{data}".encode())
        # da qui il client rimane in attesa
        mess = s.recv(BUF_SIZE).decode()
        # conferma di ricevuta del messaggio con la seguente print
        print(mess)
        # la sirena luminosa si attiva solo se è presente la seguente stringa nel messaggio
        if "ATTIVARE LA SIRENA LUMINOSA" in mess:
            sirena.up()
        # aspetta fino al prossimo giro di messaggi
        time.sleep(FREQUENZA_MESSAGGIO)

    # print(datetime.datetime.now())


if __name__ == "__main__":
    main()
