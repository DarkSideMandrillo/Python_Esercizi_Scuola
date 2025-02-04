import socket
BUFFER_SIZE = 4096
# funzione che richiamo dopo nel while de client e la eseguo solo se il comando del server non è exit
def calcola(operazione):
    try:
        # Esegue il calcolo richiesto dal server  utilizzando la funzione consigliata eval()
        risultato = str(eval(operazione))
        return risultato
    except Exception as errore:
        return f"Errore: {str(errore)}"
    
#funzione per accendere il client
def client_on():
    # Configurazione del socket client con il protocollo tcp
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    #ciclo infinito cosi il client fa le operazioni per sempre senza mai stopparsi tranne quando riceve la stringa exit
    while True:
        # Ricevi l'operazione dal server
        operazione = client.recv(BUFFER_SIZE).decode()
        
        # Verifica se è il comando di uscita
        if operazione == "exit":
            break
        #da come risultato il risultato della funzione calcola 
        risultato = calcola(operazione)
        # Invia il risultato al server
        client.sendall(risultato.encode())
    
    # Chiudo connesssione al server
    client.close()

if __name__ == "__main__":
    client_on()