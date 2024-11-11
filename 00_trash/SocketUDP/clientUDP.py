import socket

# UDP (User Datagram Protocol)
# Crea un socket UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Imposta l'indirizzo e la porta del server
server_address = ("localhost", 12345)

# Messaggio da inviare | La codifica è unicode, deve essere trasformata in utf-8
message = b"Ciao, server UDP!"  # trasforma la stringa da Unicode a formato byte
# message = "Ciao, server UDP!".encode("utf-8")

try:
    # Invia il messaggio al server
    print(f"Invio: {message}")
    # print("Invio: " + str(message))
    # print("Invio: {}".format(message))

    udp_client_socket.sendto(
        message, server_address
    )  # Bloccante, entra in stato di attesa

    # Ricevi la risposta dal server
    data, server = udp_client_socket.recvfrom(4096)
    print(f"Risposta dal server: {data.decode()}")

finally:
    # Chiudi il socket
    udp_client_socket.close()
