import socket 
import threading
import sqlite3


# Configurazione del database SQLite
def carica_operazioni():
    # mi collego al database per leggere le oprerazioni e salvarle in una lista
    conn = sqlite3.connect("operations.db", check_same_thread=False)
    cursor = conn.cursor()
    # Query per recuperare tutte le operazioni
    cursor.execute('''SELECT client, operation 
                      FROM operations ORDER BY id''')
    operazioni = {}
     # ciclo per mettere turre le operazioni che ci sono nel database   in una lista
    for client, operazione in cursor.fetchall():   #fatchall per restituire le operazioni che ho fatto
        if client not in operazioni:
            operazioni[client] = []
        operazioni[client].append(operazione)
    
    conn.close()
    return operazioni
#funzione per accendere il server
def server_on():
     # Configurazione e creazione del socket server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost',12345))
    server.listen(5)
    print("Server in ascolto su localhost sulla porta 12345:")

    #metto l'operazione nel database
    operazioni = carica_operazioni()
    # Contatore per identificare i thread
    contatore_threads = 1
    #fino a quando ci sono delle connesioni faccio andare i threads
    while True:
        conn, addr = server.accept() #accetto le connessioni dei client
        
        id_client = contatore_threads
        operazioni_del_client = operazioni.get(id_client, []) #dico quale opreazione fare per quel client 
        
        # Crea e avvia un thread per gestire il client
        thread = threading.Thread(target=gestione_client, args=(conn, addr, operazioni_del_client, contatore_threads)) #creo il thread usando il metodo che ci ha dato
        thread.start() #parte il thread (start)
        contatore_threads = contatore_threads + 1 #incremento il contatore 
#funzione per gestire il client a cui passo l'indirizzo della connessione composto da ip e porta, le operazioni del client
def gestione_client(conn, addr, operazioni_del_client, thread_id):
    client_ip, client_port = addr
    try:
        # Invia le operazioni al client
        for operazione in operazioni_del_client:
            conn.sendall(operazione.encode())
            # Ricevi il risultato dal client
            risultato = conn.recv(4096).decode()
            # Stampa il risultato come richiesto
            print(f"{operazione} = {risultato} from {client_ip} - {client_port}")
        # Invia il comando di uscita dopo che ho fatto tutte le operazioni
        conn.sendall("exit".encode())
    #eccezione per controllare i threads
    except Exception as e:
        print(f"Errore nel thread {thread_id}: {e}")
    #finito tutto smetto di trasmettere 
    finally:
        conn.close()

#creo il main dove avvio il server
if __name__ == "__main__":
    server_on()



