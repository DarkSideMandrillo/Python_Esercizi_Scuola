import socket
import datetime
import time

SERVER_ADDRESS = ("127.0.0.1", 9999)
BUFFER_SIZE = 4096
SIRENA = False


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(SERVER_ADDRESS)  # Mi connetto con il server
        print("Connesso al serverr")

        # Risultato datetime.datetime.now() -> 2024-11-18 13:01:08.087903
        data_e_ora = str(datetime.datetime.now()).split(
            " "
        )  # Spacchetto data e ora trasformandolo in stringa
        data = data_e_ora[0]
        ora = data_e_ora[1]
        print(data)
        print(ora)
        #!! la data deve essere aggiornata a ogni invio

        while True:
            inp = input(
                "Inserisci livello e id_stazione tra |: "
            )  #!! id stazione non cambia. non mettere complessita all'utente
            message = inp + "|" + data + "|" + ora
            # print(message)
            s.sendall(message.encode())  # Mando il messaggio con tutte le info
            response_from_server = s.recv(
                BUFFER_SIZE
            ).decode()  # Mi ricevo la risposta dal server inerente al livello che ho mandato

            if (
                response_from_server == "Attivare la sirena!"
            ):  # Se mi arriva il messaggio dal server che devo accendere la sirena, allora metto sirena a True
                SIRENA = True
            print("Sirena on")

            s.settimeout(15)  # Attesa 15 secondi prima di ricominciare

    except (
        ConnectionError
    ) as e:  # Se c'è qualsiasi errore inerente alla connessione allora ->
        print(f"Errore di connessione: {e}")


if __name__ == "__main__":
    main()
