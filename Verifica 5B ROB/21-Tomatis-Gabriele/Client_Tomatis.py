import socket

class DistributedClient:
    def __init__(self, host='localhost', port=65535):
        #Con questo codice eseguo la configurazione del socket client
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def run(self):
        """
        Gestisce la comunicazione con il server
        Riceve operazioni, le calcola e restituisce i risultati
        """
        try:
            while True:
                #Riceve l'operazione dal server
                operation = self.client_socket.recv(1024).decode('utf-8')
                #Verifico se è il segnale di chiusura
                if operation == 'exit':
                    break
                
                try:
                    #Calcolo dell'operazione utilizzano eval
                    result = str(eval(operation))
                    
                    #Invio il risultato al server
                    self.client_socket.send(result.encode('utf-8'))
                
                except Exception as e:
                    #Gestisco i possibili errori di calcolo
                    self.client_socket.send(str(e).encode('utf-8'))
        
        except Exception as e:
            print(f"Errore nel client: {e}")
        
        finally:
            #Chiusura della connessione
            self.client_socket.close()
            print("Connessione client chiusa.")

if __name__ == '__main__':
    client = DistributedClient()
    client.run()