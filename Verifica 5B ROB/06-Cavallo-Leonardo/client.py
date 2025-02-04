import socket

# connessione con il server
def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))

    try:
        while True:
            # il client riceve l'operazione da eseguire dal server
            operation = client.recv(1024).decode('utf-8')
            if operation == "exit":
                print("client terminato")
                break
            try:
                result = eval(operation)
            except Exception as e:
                result = f"errore: {e} "

            # invio il risultato ottenuto al server
            client.send(str(result).encode('utf-8'))
    finally:
        client.close()

if __name__ == "__main__":
    client_program()

