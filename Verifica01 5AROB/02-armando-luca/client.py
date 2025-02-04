import socket
import time
import datetime

SERVER_ADDRESS = ("127.0.0.1", 8000)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creo il socket
    s.connect(SERVER_ADDRESS)
    print("connesso al server")
    id = 2
    
    while True: 
        time.sleep(15) #per fare inviare ogni 15 secodni
        livello_acqua = 50
        data_ora = datetime.datetime.now() #funzione per data e ora attuali
        
        stringa = f"{livello_acqua}|{data_ora}|{id}" #creo la stringa da inviare al server
        messaggio = stringa.encode()
        s.sendall(messaggio)
        
        risposta = s.recv(BUFFER_SIZE).decode() #ricevo risposta dal server
        print(f"risposta del server: {risposta}") 
        
        if risposta == "attiva sirena": #controllo la risposta nel caso bisogna accendere la sirena
            print("attivazione della sirena")
        
if __name__ == "__main__":
    main()
