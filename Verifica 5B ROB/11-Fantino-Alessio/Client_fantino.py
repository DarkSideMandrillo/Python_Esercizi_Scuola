# client 1

import socket

def start_client(host='127.0.0.1', port=12345):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        
        while True:
            # ricevo l'operazione dal client 
            data = client.recv(1024).decode('utf-8')
            
            if data.lower() == "exit":  # controllo se il dato passato = exit allora termino il programma 
                #print("\nConnessione terminata dal server")
                break
            
            try:
                # controllo dell'operazione, nel caso in cui sia giusta(operazione matematica) la eseguo
                result = str(eval(data)) #  ho eseguito l'perazione con eval e la converto in stringa per essere inviata nuovamente al server 
            except Exception as e:
                result = f"\nErrore: {e}" # se non riesce ad eseguire l'operazione mando l'errore, in questo caso dovrebbe gestire l'eccezione per il secondo client dove c'è una lettera nell'operazione
            
            # invio il risultato al server
            client.send(result.encode('utf-8'))
    
    except Exception as e:
        print(f"\nErrore nel client: {e}") # gestisco anche un eccezione per l'accesso al client 
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
