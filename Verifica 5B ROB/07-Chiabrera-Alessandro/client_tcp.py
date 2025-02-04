import socket

HOST_SERVER = '127.0.0.1'  # indirizzo ip del server (host locale)
PORTA_SERVER = 65000       # porta del server

def main():
    """
    si connette al server, riceve operazioni da eseguire,
    calcola i risultati e li restituisce al server.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# creazione del socket per connessione al server
    client.connect((HOST_SERVER, PORTA_SERVER))  # connessione al server
    print(f"Connesso al server {HOST_SERVER}:{PORTA_SERVER}")

    while True:
        operazione = client.recv(4096).decode()# riceve un'operazione dal server
        if operazione.lower() == 'exit':  # verifica il comando di terminazione
            print("Terminazione richiesta dal server.")
            break

        try:
            risultato = str(eval(operazione))# eseguo l'operazione usando eval per trasformare la variabile in stringa
        except Exception as errore:
            risultato = f"Errore: {errore}"# gestisce eventuali errori nell'esecuzione dell'operazione

        client.sendall(risultato.encode())# invio il risultato al server

    client.close()  # chiude la connessione

if __name__ == "__main__":
    main()
