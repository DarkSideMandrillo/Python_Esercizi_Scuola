import time
import socket
import datetime

SERVER_ADDRESS = ("127.0.0.1", 9080)
BUFFERSIZE = 4096


def send_request(request):
    print(request)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(SERVER_ADDRESS)
    client.sendall(request.encode())
    response = client.recv(BUFFERSIZE).decode()
    return response


def main():
    while True:
        data = 15  # data di prova
        livello = float(input("Inserisci il livello del fiume: "))
        stazione = int(
            input("Inserisci l'id della stazione: ")
        )  #!! La stazione non cambia dopo l'accensione
        request = f"{data}:{livello}:{stazione}"
        response = send_request(request)  #!! quanti socket crei? e non li distruggi mai
        print(response)
        time.sleep(15)


if __name__ == "__main__":
    main()
