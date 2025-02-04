import socket
import sqlite3
import threading

BUFFER_SIZE = 4092

def funzione (client_address, client_socket, dati_database, contatore): # mi serve client address per la stampa di che client ha fatto l'operazione, client_socket per la connessione, i dati del database per sapere a chi associare le operazioni e le operazioni stesse e il contatore per associare il client al client che è in esecuzione
    #ciclo su operazioni che contiene i dati del database
    for i in dati_database:
        client = i[1]  #prendo il numero salvato nel campo client per sapere quali operazioni far fare al mio thread che è nuemerato da contatore
        if client == contatore:
            operaration = i[2] #mi salvo l'operazione da fare 
            client_socket.sendall(operaration.encode())  #la mando al client
            result = client_socket.recv(BUFFER_SIZE).decode() #mi salvo il risultato elaborato dal client
            print(f"{operaration} = {result} from {client_address[0]} - {client_address[1]}")  #stampo il risultato ottenuto
    #quando il mio ciclo è finito mando exit al client così può chiudere la connessione
    client_socket.sendall("exit".encode())
    #chiudo anche dal server la connessione con il client e con il database
    conn.close()
    client_socket.close()

#mi connetto al database   
conn = sqlite3.connect("operations.db",check_same_thread=False)
cur = conn.cursor()
#query in cui mi salvo i dati presenti nel database
cur.execute(''' SELECT id, client, operation FROM OPERATIONS''')
conn.commit()
result = cur.fetchall() #mi salvo i dati 

#apro la connessione
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 6981))
server_socket.listen(5) #sto in ascolto
print("sono in ascolto sulla porta 6981...")
cont = 1 #mi imposto il contatore fuori dal ciclo se no ogni volta mi si azzera, servirà per salvare il numero del thread che parte
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connessione cont {client_address}")
    x = threading.Thread(target=funzione, args=(client_address, client_socket, result, cont))
    x.start()
    #nel caso specifico ho due client che devono fare le operazioni per cui ho un contatore che mi identifica se sono nel primo o nel secondo trhead e di conseguenza assegna nella funzione al client le operazioni da fare
    #visto che ho solo due client se ho 1 allora lo porta a due se no vuol dire che sono già a due e quindi lo riporta a uno nel caso dovessi rifare le operazioni dell'uno
    if cont==1:
        cont+=1
    elif cont==2:
        break # i miei due thread sono partiti e hanno fatto le operazioni, per cui chiudo il while true

server_socket.close() #chiudo il socket
