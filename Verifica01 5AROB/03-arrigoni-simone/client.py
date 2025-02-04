import socket
import time
import random
import datetime

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
ATTESA = 15 #tempo di attesa tra un messaggio e l'altro
def accendi_sirena():
    '''funzione che gestisce l'accensione della sirena'''
    print("sirena accesa")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creazione socket
    s.connect(SERVER_ADDRESS)#connessione al server
    message_id = "3"
    s.sendall(message_id.encode())
    while True:
        risposta = ""
        message = f"25.2|{datetime.datetime.now()}"#messaggio da mandare al server
        time.sleep(ATTESA)#attesa tra un messaggio e l'altro
        s.sendall(message.encode())#invio del messaggio
        risposta = s.recv(BUFFER_SIZE).decode()#ricezione risposta del server

        if risposta == "richiesta attivazione sirena luminosa":#controllo che se il server mi chiede di accendere la sirena
            sirena = accendi_sirena()
        print(risposta)

if __name__ == "__main__":
    main()