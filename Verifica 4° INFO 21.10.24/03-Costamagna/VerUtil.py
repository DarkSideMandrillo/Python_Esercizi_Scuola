def inserisci_corso(nome_universita, nuovo_corso):

    universita[nome_universita]["corsi_famosi"].append(nuovo_corso)
    print(f"Corsо '{nuovo_corso}' aggiunto all'università '{nome_universita}'.")


def universita_migliore():
    universita_migliore = None
    
    for nome, info in universita():
        if info["classifica_mondiale"] > classifica_alta: 
            classifica_alta = info["classifica_mondiale"]
            universita_migliore = nome
            
    print(f"L'università con la classifica più alta è: {universita_migliore}")


def elimina_universita(nome_universita):
    del universita[nome_universita] 
    print(f"Università '{nome_universita}' eliminata.")
