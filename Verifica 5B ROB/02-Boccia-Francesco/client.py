# FRANCESCO BOCCIA - 5BROB - 28/11/2024

import socket


# funzione principale per il client
def avvio_client():

    # crea il socket client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # si connette al server sulla porta specificata
    client.connect(("localhost", 12345))

    try:

        while True:

            # riceve l'operazione dal server
            operation = client.recv(4096).decode()

            # se il server invia il segnale di chiusura, termina il ciclo
            if operation == "exit":

                print("Chiusura del client.")
                break

            try:

                # calcola il risultato dell'operazione usando eval
                result = eval(operation)

                # invia il risultato calcolato al server
                client.sendall(
                    str(result).encode()
                )  #!! Sarebbe meglio trasformare in stringa

            except Exception as e:

                # gestisce eventuali errori durante il calcolo
                client.sendall(f"Ho riscontrato l'errore: {e}".encode())

    finally:

        # chiude la connessione col server
        client.close()


if __name__ == "__main__":
    avvio_client()
