
def inserisci_corso():
    
    nome = input("Inserisci il nome della nuova università: ")

    paese = input("Inserisci il paese: ")
    
    anno_fondazione = int(input("Inserisci l'anno di fondazione: "))
    
    numero_studenti = int(input("Inserisci il numero di studenti: "))
    
    corsi_famosi = input("Inserisci i corsi famosi (separati da virgola): ").split(',')
    
    classifica_mondiale = int(input("Inserisci la classifica mondiale: "))

    universita[nome] = {
        
        "paese": paese,
        "anno_fondazione": anno_fondazione,
        "numero_studenti": numero_studenti,
        "corsi_famosi": [corso.strip() for corso in corsi_famosi],
        "classifica_mondiale": classifica_mondiale
    }
    print(f"{nome} è stata aggiunta con successo!")


def universita_piu_alta():
    
    nome_alta = None
    
    classifica_alta = float('inf')

    for nome, info in universita.items():
    
        if info["classifica_mondiale"] < classifica_alta:
    
            classifica_alta = info["classifica_mondiale"]
    
            nome_alta = nome

    print(f"L'università più alta in classifica è: {nome_alta}")


def elimina_universita(nome_universita):

    if nome_universita in universita:

        del universita[nome_universita]

        print(f"{nome_universita} è stata eliminata con successo!")

    else:

        print(f"{nome_universita} non è presente nel dizionario delle università.")