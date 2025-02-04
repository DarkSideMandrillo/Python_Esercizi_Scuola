### SERVER
import socket
import sqlite3
import threading


class ServerCalcoloDistribuito:
    def __init__(self, host="localhost", port=12346):
        """
        server Verifica (CalcoloDistribuito)
        Parametri:
        Local Host
        porta 12346

        """
        self.host = host
        self.port = port
        self.operazioni = []  # lista salvataggio operazioni
        self.contatore_thread = 0  # contatore per i thread dei client
        self.carica_operazioni_da_db()

    def carica_operazioni_da_db(
        self,
    ):  # funzione che carica le operazioni dal database e le salva in mem (lista)

        conn = sqlite3.connect(
            "operations.db", check_same_thread=False
        )  # connessione a operations(database)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, client, operation FROM operations ORDER BY client"
        )  # query database
        self.operazioni = cursor.fetchall()  # salvataggio con successiva chiusura
        conn.close()

    def gestisci_client(
        self, connessione, indirizzo_client
    ):  # funzione che gestisce la comunicazione con un singolo client.

        self.contatore_thread += 1
        numero_thread = self.contatore_thread
        operazioni_client = [
            op for op in self.operazioni if op[1] == numero_thread
        ]  # operazione che filtra le operazione del singolo client in base al numero di thread
        try:
            for operazione in operazioni_client:
                id_operazione, client_id, formula = operazione
                connessione.sendall(formula.encode())
                risultato = connessione.recv(4096).decode()

                print(
                    f"{formula} = {risultato} from {indirizzo_client[0]} - {indirizzo_client[1]}"
                )  # stampa del risultato con il pattern
                # formula=operazione
            connessione.sendall("exit".encode())

        except Exception as e:  # ECCEZIONE per errore server sporco con stringa
            print(f"Errore nel thread {numero_thread}: {e}")
        finally:
            connessione.close()

    def avvia_server(self):  # avvia il server per il client
        server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # crea server TCP
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)  # ascolto, max 5 connesioni
        print(f"Server in ascolto su {self.host}:{self.port}")

        while True:
            connessione, indirizzo_client = server_socket.accept()
            thread_client = threading.Thread(  # creazione thread per gestire il client
                target=self.gestisci_client, args=(connessione, indirizzo_client)
            )
            thread_client.start()


if __name__ == "__main__":
    # creazione, avvio del server
    server = (
        ServerCalcoloDistribuito()
    )  #!! si ma. Le classi identificano degli oggetti. Non tutto il codice
    server.avvia_server()
