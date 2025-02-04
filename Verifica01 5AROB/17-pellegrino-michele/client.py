"""
messaggi-> "misurazione|data|ora|id"
ogni 15 secondi 1 messaggio
"""
import datetime
import socket
import time
SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

attesa = 1
def sirena_on():
    print("SIRENA ACCESA")

def sirena_off():
    print("SIRENA SPENTA")
    
def main():
    sirena = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    id = input("Inserisci l'id della stazione\n> ")
    while True:
        date = datetime.datetime.now()
        dataora = str(date).split(".")
        dataorasplit = str(dataora).split(" ")
        data = dataorasplit[0][2:]
        ora = dataorasplit[1][:-2]

        misurazione = float(input("Inserisci il valore del livello del fiume\n> "))
        s.sendall(f"{misurazione}|{data}|{ora}|{id}".encode())
        message = s.recv(BUFFER_SIZE)
        message = message.decode().split("|")
        if message[0] == "0":
            print(message[1])
            if sirena:
                sirena_off()
        else:
            if sirena == False:
                sirena_on()
        time.sleep(attesa)

if __name__ == "__main__":
    main()