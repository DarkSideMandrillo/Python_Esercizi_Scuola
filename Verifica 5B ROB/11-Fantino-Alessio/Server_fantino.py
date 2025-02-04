import socket
import threading
import sqlite3


DB_PATH = "./operations.db" #path del db

# gestisco la connessione dei client= 
def gestione_client(client_socket, client_address, operations, thread_id): # gli passo socket usato per comunicare col client,una tupla contenente ip e porta del client, operazione presa dal database e id del thread 

    try:
        # ottengo le  operazioni per il client corrente( 1/2)-- devo eseguirlo 1 alla volta cambiando thread-id--
        client_operations = [op for op in operations if op[1] == thread_id]
        
        for operation in client_operations:
            operation_id, client_id, expression = operation
            
            # invio l'operazione al client
            client_socket.send(expression.encode('utf-8'))
            
            # ricevo il risultato dal client che ha eseguito l'operazione e convertita in stringa
            result = client_socket.recv(1024).decode('utf-8')
            
            print(f"{expression} = {result} from {client_address[0]} - {client_address[1]} ") # stampo il risultato, dato che client_address è una tupla accedo ai risultati con indice 

        
        # invio il comando di chiusura al client
        client_socket.send("exit".encode('utf-8'))
    
    except Exception as e: #gestisco l'eccezione dove non viene eseguito il thread 
        print(f"Errore nel thread {thread_id}: {e}")
    finally:
        client_socket.close()



# leggo le operazioni dal database

def carica_operazioni():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM operations;")
        operazione = cursor.fetchall()
        return operazione #returno l'operazione ottenuta con la query


# conf del server 
def start_server(host='127.0.0.1', port=12345): 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    #print(f"\n Server in ascolto su {host} : {port}")
    
    operations = carica_operazioni()
    thread_id = 1 # identificatore dell' id client, devo cambiarlo per accedere alle operazioni del client 2 , ?
    
    while True:
        client_socket, client_address = server.accept()
       # print(f"Connessione accettata da {client_address[0]}:{client_address[1]}")
        
        # avvio un nuovo thread per il client
        client_thread = threading.Thread(target=gestione_client, args=(client_socket, client_address, operations, thread_id))
        client_thread.start() # eseguo il thread contenente la funzione per gestiere la connessione dei client e invio/ricevimento dati 
        
        thread_id = thread_id +1 #porto id client a 2 --?


if __name__ == "__main__":
    start_server() #starto il server 

