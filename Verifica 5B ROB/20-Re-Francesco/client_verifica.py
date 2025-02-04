import socket as s

SERVER_ADDRESS = ("0.0.0.0", 12345)
BUFFER_SIZE = 4096

client_tcp = s.socket(s.AF_INET, s.SOCK_STREAM)
try:
    client_tcp.connect(SERVER_ADDRESS)
except Exception:
    # se non riesco a collegarmi mando una stringa di errore
    print("print connessione non riuscita!!")
finally:
    while True:
        operation = client_tcp.recv(BUFFER_SIZE).decode("utf-8")
        # se non funziona la stringa che il server manda, allora mando al server un errore
        try:
            if operation != "exit":
                result = eval(operation)
                client_tcp.send(f"{result}".encode("utf-8"))
            else:
                break
        except Exception:
            client_tcp.send(
                f"{operation} non è un'operazione valida !!!".encode("utf-8")
            )
    client_tcp.close()
