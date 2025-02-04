import socket

address=('localhost',2222)
buffer_size=4096 #numero massimo dei byte che posso ricevere

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creo un oggetto client

client.connect(address) #mi connetto al server 

valoriSporchi='qwertyuiopasdfghjklzxcvbnm?^!£$%&' #creo una stringa di valori sporchi, quindi valori che nn dovrei ricevere
def puliziaStringa(strSporca): #funzione che rimuove, se presenti, i caratteri sporchi da una stringa
    # print(strSporca)
    for i in valoriSporchi:
        # print(i)
        strSporca=strSporca.replace(i,'') #rimuovo i caratteri non utili e sostituendoli con un carattere vuoto
    # print(strSporca)
    return strSporca #restituisco la stringa pulita



while True:
    try:
        stringa=client.recv(buffer_size).decode('utf-8') #ricevo dal server un comando

        if stringa=='exit': #se ricevo exit fermo tutto e chiudo la connessione
            break
        stringa=puliziaStringa(stringa)  #pulisco la stringa
        risultato=eval(stringa) #faccio l'eval della stringa ottenuta come operazione
        client.sendall(str(risultato).encode('utf-8')) #mando il risultato al server
    except(TimeoutError, RuntimeError):
                print(f'errore con il dispositivo')


client.close() #chiudo la connessione