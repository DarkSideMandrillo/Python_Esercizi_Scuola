import socket

class ClientCalcoloDistribuito:
    def __init__(self, host='localhost', port=12346):
        """
        client Verifica (CalcoloDistribuito)
        Parametri:
        Local Host
        porta 12346
        """
        self.host = host 
        self.port = port 
    
    def connetti_e_calcola(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creazione client tcp
            client_socket.connect((self.host, self.port))
            
            while True:
                operazione = client_socket.recv(4096).decode()
                if operazione == "exit":
                    break
                
                try:
                    risultato = str(eval(operazione))#calcolo risultato con EVAL
                    client_socket.sendall(risultato.encode())
                
                except Exception as e:
                    client_socket.sendall(str(e).encode())#in caso di errore manda stringa
        
        except ConnectionRefusedError:
            print("Errore connesione server")
        
        except Exception as e:
            print(f"Errore generico: {e}")
        
        finally:
            client_socket.close()

if __name__ == "__main__":
    # Creazione e avvio del client
    client = ClientCalcoloDistribuito()
    client.connetti_e_calcola()
