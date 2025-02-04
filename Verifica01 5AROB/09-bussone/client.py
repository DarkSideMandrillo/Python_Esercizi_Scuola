import socket
import time
import datetime

INDIRIZZO_SERVER = ("localhost", 7777)
BUFFER = 4096
TEMPO_DI_INVIO = 15 

def main():
    try:
        #connessione utilizzando il protocollo tcp 
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        client_socket.connect(INDIRIZZO_SERVER)

        #prendo in input l'id della stazione 
        id_stazione = input("inserisci l'ID della stazione desiderata: ")

        while True:

            livello = 2
            data_e_ora = datetime.datetime.now() #restituisce l'ora e data aggiornata e salvo tutto nella variabile 
            messaggio = f"{id_stazione};{livello};{data_e_ora}" # stampo il messaggio con le informazioni richieste

            #inivio i dati necessari al server
            client_socket.sendall(messaggio.encode())
            print(f"Livello inviato: {messaggio}")

            #ricevo i dati in risposta al server 
            rostispa = client_socket.recv(BUFFER).decode()
            print(f"Risposta dal server: {risposta}")

            #atttivazione della sirena nel caso in cui il livello è >= al 70%
            if "richiesta attivazione sirena" in risposta:
                print("!!!!!!!!!!!!!!sirena.up()!!!!!!!!!!!!!!")
            elif "ricerca stazione con esito NEGATIVO" in risposta:
                print(f"errore nella ricerca dei dati nel databse")

            time.sleep(TEMPO_DI_INVIO) #tempo di inivio dei messaggi configurabile manualmente 

    finally:
        client_socket.close()  #chiusura della connessione

if __name__ == "__main__":
    main()