import socket
import datetime
import time
import random as np  #!!?

# indirizzo e porta del server oltre alla dimensione massima del buffer
SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


def main():
    n = input(
        "Inserisci il valore di timeout per gestire la frequenza di invio: "
    )  #!! stringa
    # creato un client per il server facciamo in modo che lo user
    # possa inviare tramite protocollo ideato da me, le informazioni necessarie
    print(
        """Protocollo di comunicazione:
                verificaLivello|livello|dataOra|idStazione
                exit
          """
    )
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    while True:
        time.sleep(n)
        # invio la stringa formattata al server
        richiesta, livello, dataOra, idStazione = (
            "verificaLivello",
            np.random.randint(0, 11),
            str(datetime.datetime.now()),
            np.random.randint(0, 11),
        )
        s.sendall(f"{richiesta}|{livello}|{dataOra}|{idStazione}".encode())
        messaggio = s.recv(BUFFER_SIZE)
        messaggio = messaggio.decode()
        # ricevo la risposta dal server e la stampo a video per l'utente
        print(f"Ricevuto <{messaggio}> dal server")
        # nel caso in cui il messaggio sia per terminare la comunicazione
        if messaggio == "comunicazione terminata":
            # blocchiamo il client
            break
        elif "DANGER" in messaggio:
            # sirena.app(HIGH)
            print("Accensione Sirena Luminosa.")
            pass
    s.close()


if __name__ == "__main__":
    main()
