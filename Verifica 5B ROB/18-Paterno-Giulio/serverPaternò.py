###SERVER:
#Includo le librerie necessarie
import socket
import sqlite3
from threading import Thread

indirizzo_server = '127.0.0.1' #Indirizzo del server
porta = 22223 #Porta del server

#Definisco una funzione che mandi le operazioni al client
def rispondi_client(client, indirizzo_client, operazioni):
    try: #Per la gestione di eccezioni e errori
        #Ricevo l'ID del client
        client_id = client.recv(4096).decode('utf-8').strip()
        print(f"ID ricevuto dal client: {client_id}") #Stampo l'ID
        
        #Filtro le operazioni da eseguire secondo l'ID del client
        operazioni_da_eseguire = operazioni.get(int(client_id), [])
        
        #Con un ciclo for scorro tutte le operazioni da eseguire per il client trovato
        for operazione in operazioni_da_eseguire:
            #Invio l'operazione da eseguire al client
            client.sendall(operazione.encode('utf-8'))

            #Ricevo il risultato dal client
            risultato = client.recv(4096).decode('utf-8')

            #Stampo il risultato ottenuto dal client
            print(f"{operazione} = {risultato} from {indirizzo_client[0]} - {indirizzo_client[1]}")

        #Il server invia il comando "exit" al client per terminare la connessione
        client.sendall("exit".encode('utf-8'))
    #Errore eventuale restituito
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        client.close() #Chiude la connessione

def main():
    #Eseguo la connessione al database
    conn = sqlite3.connect('./operations.db', check_same_thread=False)
    cursor = conn.cursor()
    
    #Eseguo l'interrogazione al database per ricavare l'operazione da eseguire e il client a cui mandarla
    cursor.execute('''
        SELECT operation, client
        FROM operations
    ''')
    operazioni_client = cursor.fetchall() #Salvo i dati ottenuti
    
    #Creo un dizionario che ha per chiave l'id del client e per valore la lista di operazioni da eseguire
    operazioni_dizionario = {}
    for operazione, client in operazioni_client:
        if client not in operazioni_dizionario:
            operazioni_dizionario[client] = [] #Se l'ID non è presente nel dizionario lo aggiunge
        operazioni_dizionario[client].append(operazione) #Se è presente aggiunge l'operazione alla lista di operazioni

    conn.close()  #Chiudo la connessione col database perché ho salvato tutte le informazioni necessarie

    #Creo il socket del server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Uso il TCP
    server.bind((indirizzo_server, porta))
    server.listen(5)
    print("Server in ascolto...") #Messaggio visualizzato nel momento in cui nessun server è ancora connesso al server

    #Ciclo while True er la gestione dei client
    while True:
        client, indirizzo_client = server.accept()
        print(f"Connessione dal client: {indirizzo_client}")
        
        #Creo un thread per gestire il client
        client_thread = Thread(target=rispondi_client, args=(client, indirizzo_client, operazioni_dizionario))
        client_thread.start()

if __name__ == "__main__":
    main()
