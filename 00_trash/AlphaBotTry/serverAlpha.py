import socket

BUFFER_SIZE = 4092
SERVER_ADDRESS = ("localhost", 6030)


def main():

    command_list = {
        0: "Exit",
        1: "Forward",
        2: "Backward",
        3: "Left",
        4: "Right",
    }

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(SERVER_ADDRESS)

    tcp_server_socket.listen(1)
    print("Server in attesa di connessioni")
    conn, address = tcp_server_socket.accept()  # Bloccante
    print(f"Connessione stabilita con {address}")

    while True:
        try:
            command_recv = conn.recv(BUFFER_SIZE)  # Bloccante
            command_recv = command_recv.decode()
            command_recv = command_recv.split("|")

            command_key = int(command_recv[0])  # Trasformo in INT o sollevo eccezione
            command_value = int(command_recv[1])

            if command_key in command_list:
                if command_key == 1:
                    conn.sendall(
                        f"Command -> {command_list[command_key]} | Value -> {command_value}".encode()
                    )
                elif command_key == 2:
                    conn.sendall(
                        f"Command -> {command_list[command_key]} | Value -> {command_value}".encode()
                    )
                elif command_key == 3:
                    conn.sendall(
                        f"Command -> {command_list[command_key]} | Value -> {command_value}".encode()
                    )
                elif command_key == 4:
                    conn.sendall(
                        f"Command -> {command_list[command_key]} | Value -> {command_value}".encode()
                    )
                elif command_key == 5:
                    conn.sendall(
                        f"Command -> {command_list[command_key]} | Value -> {command_value}".encode()
                    )
                elif command_key == 0:
                    conn.sendall(f"Chiusura connessione".encode())
                    break
        except:
            print("error")
            tcp_server_socket.close()
            break

        finally:
            tcp_server_socket.close()
            print("Connessione chiusa.")


if __name__ == "__main__":
    main()
