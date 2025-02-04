import socket
import time
import random
import datetime

SERVER = "127.1.1.1"
PORT = 8000
ID_STAZIONE = 1

def genera_livello_misurato():
    return random.uniform(0, 20)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"Connesso al server {SERVER}:{PORT}")
    intervallo = 15 
    print("PROVA")
    while True:
        livello = genera_livello_misurato
        messaggio = {
           "ID STAZZIONE: " : ID_STAZIONE,
            "LIVELLO ": livello,
            "Data e ora" : time = datetime.datetime.now() #!! Errore di sintassi
        }
        
        client.send(str(messaggio).encode)
        risposta = client.recv(1024).decode()
        print(f"Risposta dal server: {risposta}")
            
        if risposta == "allarme":
            for i in 100:
                print("SIRENA ATTIVATA")
                time.sleep(0.5)
            
        time.sleep(intervallo)
        print("PROVA1")

if __name__ == "__main__":
    main()
