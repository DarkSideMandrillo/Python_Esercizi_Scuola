import socket

# Crea un socket UDP
udp_server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
)  # AF_INET Address Family - Internet. è il formato ipv4

# Associa il socket a un indirizzo e una porta
server_address = ("localhost", 12345)
udp_server_socket.bind(server_address)

print("Server UDP in ascolto...")

while True:
    # Ricevi dati dal client
    data, address = udp_server_socket.recvfrom(4096)  # Bloccante

    print(f"Messaggio ricevuto: {data.decode()} da {address}")

    # Invia una risposta al client
    if data:
        response = b"Messaggio ricevuto!"
        udp_server_socket.sendto(response, address)
