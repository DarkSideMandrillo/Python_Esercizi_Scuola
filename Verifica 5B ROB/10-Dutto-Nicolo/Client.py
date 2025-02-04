import socket 

def avvia_client():
    #creo il socket del client
    server_ip = 'localhost'
    port = 12345
    address = (server_ip, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    print('connessione stabilita con il server')


    while True:
        operazione = client_socket.recv(1024).decode()
        #controllo se la stringa vuole chiudere la connessione
        if operazione == "esci":
            #print("il server ha chiuso la connessione")
            break
        #eseguo  l'operazione ricevuta dal  sevrer
        try:    #provo ad eseguirla
            risultato = str(eval(operazione))
        except Exception as exc: #se si verifica un eccezione segnalo al client un errore
            risultato = f"errore: {str(exc)}"
            
        #invio il risultato al server
        client_socket.send(risultato.encode())
        
    #chiudo la connessione al client
    client_socket.close()

def main():
    avvia_client()

if __name__ == "__main__":
    main()
            



