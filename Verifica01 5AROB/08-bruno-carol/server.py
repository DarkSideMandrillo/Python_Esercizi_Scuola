import socket, threading, sqlite3

BUF_SIZE = 4096  # buffer size per la recv
MY_ADDRESS = ("127.0.0.1", 9090)  # serve per la funzione bind


class Gestore_client(threading.Thread):
    # Questa classe serve per la gestione multiclient da parte del server
    def __init__(
        self, connection
    ):  # per ogni client, avrà la propria connessione dato che uso TCP, quindi gli passo la connessione
        super().__init__()
        self.connection = connection

    def run(self):
        while True:
            mess = self.connection.recv(BUF_SIZE).decode()
            mess_split = mess.split(
                "|"
            )  # divido il messaggio che ho formattato separando i valori con "|"

            # il formato del messaggio è il seguente: "{id_stazione}|{livello_misurato}|{data}"
            id_stazione = int(mess_split[0])
            livello_misurato = float(mess_split[1])
            data = mess_split[2]

            # attivo la connessione con il db
            with sqlite3.connect(
                "fiumi.db"
            ) as db:  #!! apro la connessione a ogni messaggio e non la chiudo (anche se con with teoricamente si chiude)
                cur = db.cursor()

                # la query che eseguo mi restituisce sempre solo 1 record (tranne se l'input utente non è corretto, in quel caso è vuota la lista)
                query = cur.execute(
                    f"SELECT livello, fiume, localita FROM livelli WHERE id_stazione = {id_stazione}"
                )
                # prendo la lista dei record con fetchall()
                lista_record_livelli = query.fetchall()
                # li suddivido in 3 variabili per ogni campo che mi serve
                livello_di_guardia = lista_record_livelli[0][0]
                nome_fiume = lista_record_livelli[0][1]
                localita = lista_record_livelli[0][2]

                if (
                    livello_misurato < livello_di_guardia * 0.3
                ):  # livello_di_guardia * 0.3 rappresenta il 30%
                    self.connection.sendall("messaggio ricevuto con successo".encode())
                elif (
                    livello_misurato < livello_di_guardia * 0.7
                ):  # * 0.7 rappresenta il 70%
                    self.connection.sendall("messaggio ricevuto con successo".encode())
                    print(
                        f"PERICOLO IMMINENTE\nnome fiume: {nome_fiume}\nlocalita: {localita}\ndata e ora: {data}\n\n"
                    )
                else:  # livello_misurato > 70% livello di guardia
                    # la particolarità di questo messaggio è che è composto da "ATTIVARE LA SIRENA LUMINOSA", quindi il client farà il controllo di questa parte
                    # quindi poi attiverà la sirena di conseguenza
                    self.connection.sendall(
                        "messaggio ricevuto con successo\n\nATTIVARE LA SIRENA LUMINOSA".encode()
                    )

                    print(
                        f"PERICOLO IN CORSO\nnome fiume: {nome_fiume}\nlocalita: {localita}\ndata e ora: {data}\n\n"
                    )


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, _ = s.accept()
        thread = Gestore_client(
            connection
        )  # creazione del thread per il client con la connessione stabilita
        thread.start()


if __name__ == "__main__":
    main()
