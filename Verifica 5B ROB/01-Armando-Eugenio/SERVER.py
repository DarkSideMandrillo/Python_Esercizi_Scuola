import socket
import threading
import sqlite3

nomeDB='operations.db' #nome del db
address=('localhost',2222) #tupla contenente l'ip e la porta su cui sarà presente il socket
buffer_size=4096 #dimensione massima dei byte possibili da ricevere
numDisp=5 #numero di dispositivi massimo che posso gestire

def leggiTabellaInDB(nomeDB,nomeTabella): #legge una tabella specificata dentro un server specificato e restituisce una lista di tuple
    conn=sqlite3.connect(nomeDB,check_same_thread=False) #mi connetto al db
    cursor=conn.cursor()
    cursor.execute(f'SELECT * FROM {nomeTabella}') #faccio la query
    valori=cursor.fetchall()
    conn.close() #chiude la connessione con il db
    return valori

valori=leggiTabellaInDB(nomeDB,'operations') #richiamo la funzione leggiTabellaInDB



server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creo un oggetto di tipo socket
server.bind(address) #associo ip e porta al socket
server.listen(numDisp) #mi metto in ascolto, posso gestire massimo numDisp dispositivi




def contatta(conn,add,listaOperazioni,numeroThread): #thread, permette al server di comunicare con un client
    
    client_ip=add[0] #ricavo l'ip del socket che si è connesso
    client_port=add[1] #ricavo la porta del socket che si è connesso
    for i in listaOperazioni:
        if i[1] == numeroThread: #in posizione 1 è presente il numero del client che corrisponde al numero del thread nel mio caso
            operazione=i[2]
            #tocca a me
            #faccio la richiesta e attendo un risultato
            try:
                conn.sendall(operazione.encode('utf-8')) #mando l'operazione
                risultato=conn.recv(buffer_size).decode('utf-8') #ricevo il risultato
                print (f"{operazione} = {risultato} from {client_ip} - {client_port}") #stampo il risultato
            except(TimeoutError, RuntimeError):
                print(f'errore con il dispositivo: {add}') #do errore se viene generata un eccezzione
    #se arrivo qui significa che ho terminato 
    conn.sendall('exit'.encode('utf-8')) #invio exit per indicare che è terminata la comunicazione.
    conn.close() #chiudo la connessione


cont=0 #contiene il numero del client

def numeroMaxDiThreads(valori): #conto il numero massimo di thread che si possono collegare
    clConosciuti=[] #contiene i numeri dei client conosciuti
    for i in valori:
        numCl=i[1] #ricavo il numero del client
        if numCl not in clConosciuti:
            clConosciuti.append(numCl) #aggiungo il numero del client alla lista dei client conosciuti
    
    return len(clConosciuti) #conto la lunghezza della lista che 


numMaxTh=numeroMaxDiThreads(valori) #per capire se il server ha finito di lavorare

while numMaxTh!=cont:
    conn,add=server.accept()
    cont+=1
    thread=threading.Thread(target=contatta,args=(conn,add,valori,cont)).start()



    
