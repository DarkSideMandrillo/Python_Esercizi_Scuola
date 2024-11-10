import socket

def start_client(host='127.0.0.1', port=12345):
    # Creazione del socket del client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connessione al server
        client_socket.connect((host, port))
        print(f"Connesso al server su {host}:{port}")
        
        while True:
            # Input dell'utente
            scelta = int(input("""Quale operazione vuoi fare? (o 'exit' per uscire):
                            1 - chiedere se un certo nome file è presente (input nome)
                            2 - chiedere il numero di frammenti di un file (input nome)
                            3 - chiedere l’IP dell’host che ospita un frammento (input nome, n°frammento)
                            4 - chiedere gli IP degli host sui quali sono salvati i frammenti di un file (input nome)"""))
            match scelta:
                case 1:
                    name = input("Inserisci il nome del file")
                    message = "1|" + name
                case 2:
                    name = input("Inserisci il nome del file")
                    message = "2|" + name
                case 3:
                    name = input("Inserisci il nome del file")
                    frame = input("Inserisci il numero del frammento")
                    message = "3|" + name +"|"+frame
                case 4:
                    name = input("Inserisci il nome del file")
                    message = "4|" + name
                case 'exit':
                  print("Disconnessione dal server...")
                  break                    
           
            # Invio del messaggio al server
            client_socket.sendall(message.encode())
            
            # Ricezione della risposta dal server
            response = client_socket.recv(1024)
            print(f"Risposta dal server: {response.decode()}")
    
    except ConnectionRefusedError:
        print("Connessione rifiutata dal server.")
    finally:
        # Chiusura del socket
        client_socket.close()
        print("Connessione chiusa.")

# Avvio del client
start_client()
