import socket

server_address = ("localhost", 12345)
BUFFER_SIZE = 4092

# Creazione del socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind del socket all'indirizzo IP e alla porta
server_socket.bind(server_address)

# Dizionario di client
clients = {}

print(f"Server UDP in ascolto su {server_address[0]}:{server_address[1]}")

while True:
    # Ricezione dati dal client
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    clients[client_address] = client_address

    # Cerco se c'è un altro client address
    other_client_address = [addr for addr in clients if addr != client_address]
    print(f"messaggio da {client_address}: {data.decode()}")
    if other_client_address:
        # Invia il messaggio all'altro client
        print(f"Invio a {other_client_address[0]}: {data.decode()}")
        server_socket.sendto(data, other_client_address[0])
    else:
        print("aspetto secondo client")
