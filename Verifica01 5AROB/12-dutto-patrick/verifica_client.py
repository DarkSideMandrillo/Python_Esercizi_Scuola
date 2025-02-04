from datetime import date, datetime
import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(SERVER_ADDRESS)
        print("Connesso al server.")

        while True:
            ora = datetime.datetime.now()  #!! errore di sintassi. non restituisce l'ora
            data = date.date.now()
            localita = input(
                "inserisci il nome della localita"
            )  #!! la localita non cambia a ogni invio
            livello = input("inserisci il nome livello")

            s.sendall(
                (localita, livello, ora, data).encode()
            )  # Il client invia al server i dati inseriti dall'utente.
            risposta = s.recv(BUFFER_SIZE).decode()
            if risposta == "livello troppo alto accendere la sirena luminosa":
                print("accensione sirena luminosa")
            else:
                print("risposta: ", risposta)

            s.sleep(15)

    except ConnectionError as e:  # stampa l'errore (e)
        print(f"Errore di connessione: {e}")

    finally:  # chiude la conessione una volta terminato
        s.close()
        print("Connessione chiusa.")


if __name__ == "__main__":
    main()
