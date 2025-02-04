import socket
import datetime
import time

ip_server = ("127.0.0.1", 8080)

lista_valori = [1, 3, 9, 10, 11, 9, 8, 7, 9, 10, 11, 9, 7, 5, 6, 7, 5, 2]

id = 1


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ip_server)

    adesso = datetime.datetime.now()  #!! da aggiornare ad ogni invio

    print(adesso)

    k = 0

    timer = 15

    while True:

        """
        Il messaggio arriverà come
        Identificativo|livello|data&ora
        """

        client.sendall(
            f"{id}|{lista_valori[k]%len(lista_valori)}|{adesso}".encode()
        )  #!! ?

        res = client.recv(4096)  #!! nomina meglio le variabili

        if res == "Pericolo":
            print("attivazione sirena")
            while True:
                print("NINO")
                time.sleep(1)
        elif res == "Ricevuto":
            print("Tutto apposto")
        else:
            print("messaggio non capito")
        #!! usiamo print migliori
        print(res.decode())

        time.sleep(timer)


if __name__ == "__main__":
    main()
