import threading
import socket

SERVER_ADDRESS = ("localhost", 12345)
BUFFER_SIZE = 4092


def sendText(client_socket):
    message = ""
    while message != "exit()":
        message = input()
        client_socket.sendto(message.encode(), SERVER_ADDRESS)
    client_socket.close()


def listenToServer(client_socket):
    while True:
        data, client_address = client_socket.recvfrom(BUFFER_SIZE)
        print(f"\nChatX: {data.decode()}\n")


def main():
    # Creo il socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Mando il primo messagio per salvare addr
    client_socket.sendto("".encode(), SERVER_ADDRESS)
    # Creo thread e avvio
    thread = threading.Thread(target=listenToServer, args=(client_socket,))
    thread.start()
    # Funzione per scrivere
    sendText(client_socket)


if __name__ == "__main__":
    main()
