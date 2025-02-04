import socket

# Configurazione del client
HOST = '127.0.0.1'  # Indirizzo del server
PORTA = 12345        # Porta del server

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORTA))
        

        while True:
            # Ricezione di un'operazione dal server
            operazione = client.recv(1024).decode()
            if operazione.lower() == "exit":
                print("Client 2 terminato")
                break

            
            try:
                risultato = eval(operazione)
                client.sendall(str(risultato).encode())
            except Exception as e:
                client.sendall(f"Errore: {e}".encode())

if __name__ == "__main__":
    start_client()
