import socket
import sqlite3
import threading

class DistributedServer:
    def __init__(self, host='localhost', port=65535):
        #Configuro il server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        
        #carico le operazione dal db
        self.operations = self.load_operations()
        
        #Variabile contatore per i thread
        self.thread_counter = 1

    def load_operations(self):
        """
        Carica le operazioni dal database SQLite
        Returns: Lista di tuple (id, client, operazione)
        """
        conn = sqlite3.connect('operations.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, client, operation FROM operations')
        operations = cursor.fetchall()
        conn.close()
        return operations

    def handle_client(self, client_socket, client_address):
        """
        Gestisce le comunicazioni con un singolo client
        Invia operazioni specifiche per quel client
        """
        #identificativo del thread che corrisponde al thread
        client_thread_id = self.thread_counter
        self.thread_counter += 1
        
        #filtra le operazioni per questo specifico client
        client_operations = [
            op[2] for op in self.operations if op[1] == client_thread_id
        ]
        
        try:
            #invio ogni operazione al client
            for operation in client_operations:
                # Invia l'operazione al client
                client_socket.send(operation.encode('utf-8'))
                
                #Ricevo il risultato dal client
                result = client_socket.recv(1024).decode('utf-8')
            
                print(f"{operation} = {result} from {client_address[0]} - {client_address[1]}")
            
            client_socket.send('exit'.encode('utf-8'))
        
        except Exception as e:
            print(f"Errore nella gestione del client {client_thread_id}: {e}")
        
        finally:
            client_socket.close()

    def start(self):
        """
        Avvia il server e accetta connessioni dai client
        """
        print("Server in attesa di connessioni...")
        
        while True:
            #accetta la connessione
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(
                target=self.handle_client, 
                args=(client_socket, client_address)
            )
            client_thread.start()

if __name__ == '__main__':
    server = DistributedServer()
    server.start()