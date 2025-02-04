import socket

#queste non sono le porte del client ma sono del server, quindi per far sì che venga stampata la porta del client nel server devo lavorare sul server
host_server = '127.0.0.1'
porta_server = 9081

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #creazione del socket del client
    client.connect((host_server, porta_server))    #connessione del client al server

    while True:    #cicla True ma realmente si interrompe quando sono terminate le operazioni da eseguire
        operazione = client.recv(1024).decode()    
        if operazione == "exit":       #questo viene fatto quando il server deve chiudere la connessione e quando quindi tutte le operazioni sono state eseguite
            break
        risultato = eval(operazione)
        client.sendall(str(risultato).encode())     #trasforma nuovamente il risultato in stringa

    client.close()

if __name__ == "__main__":
    main()


