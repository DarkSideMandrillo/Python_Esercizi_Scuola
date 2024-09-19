import socket

BUFFER_SIZE = 4092
SERVER_ADDRESS = ("localhost", 6030)


def main():
    try:
        tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client_socket.connect(SERVER_ADDRESS)

        while True:
            command_send = input(
                "Command:\n[1] Forward\n[2] Backward\n[3] Left\n[4] Right\n[0] Exit\n"
            )

            # Verifica se l'input è un numero valido
            if not command_send.isdigit():
                print("Comando non valido, inserisci un numero.")
                continue

            command_send = int(command_send)

            if command_send == 0:  # Exit mando l'uscita
                print("Chiusura della connessione.")
                tcp_client_socket.sendall(
                    b"0|0"
                )  # Invia un messaggio di chiusura al server
                break

            command_value = input("Value->")
            if not command_value.isdigit():
                print("Valore non valido, utilizzo 0 come predefinito.")
                command_value = 0
            else:
                command_value = int(command_value)

            # Unisci il messaggio da inviare
            message = f"{command_send}|{command_value}"
            tcp_client_socket.sendall(message.encode())

            # Aspetto la risposta
            response_message = tcp_client_socket.recv(BUFFER_SIZE)
            print("Risposta del server", response_message.decode())

            if command_send == 0:
                break

    except OSError as e:
        print(f"Errore di rete o connessione: {e}")

    finally:
        tcp_client_socket.close()
        print("Connessione chiusa.")


if __name__ == "__main__":
    main()
