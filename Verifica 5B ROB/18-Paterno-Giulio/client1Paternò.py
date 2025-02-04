###CLIENT-1:
#Includo la libreria socket
import socket

indirizzo_server = '127.0.0.1'  #Indirizzo del server
porta = 22223 #Porta del server

def main(client_id):
    #Creo il socket del client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Uso il TCP
    client.connect((indirizzo_server, porta))
    
    #Invio l'ID del client al server in modo da ricevere le corrette operazioni
    client.sendall(str(client_id).encode('utf-8'))

    #Ciclo while True per la gestione dei dati ricevuti dal server
    while True:
        operazione = client.recv(4096).decode('utf-8')

        #Se il server invia "exit" esco dal ciclo e chiudo la connessione
        if operazione == "exit":
            break

        try: #Per la gestione di eccezioni e errori
            risultato = eval(operazione) #Calcolo il risultato tramite la funzione "eval()"
            client.sendall(str(risultato).encode('utf-8'))

        #Errore eventuale restituito
        except Exception as e:
            client.sendall(f"Errore: {e}".encode('utf-8'))

    #Chiudo la connessione
    print("Connessione terminata.")
    client.close()

if __name__ == "__main__":
    main(client_id=1) #Essendo il client numero 1 l'ID passato al main deve essere uguale a 1