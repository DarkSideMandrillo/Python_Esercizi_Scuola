import socket

def main():
    HOST = '127.0.0.1'
    PORT = 65432

    try:
        # Crea il socket del client
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        while True:
            # Riceve i dati dal server
            data = client_socket.recv(4096).decode()
            if data == "exit":
                break
            
            try:
                # Calcola il risultato usando eval
                result = str(eval(data))
            except Exception as e:
                result = f"Errore: {e}"
            
            # Invia il risultato al server
            client_socket.sendall(result.encode())
    except ConnectionRefusedError:
        print("Connessione al server fallita. Assicurati che il server sia in esecuzione.")
    except Exception as e:
        print(f"Errore durante l'esecuzione del client: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
