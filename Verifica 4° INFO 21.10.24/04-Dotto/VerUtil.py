def aggiungi_corso(universita, nome_universita, nuovo_corso):
    if nome_universita in universita:
        universita[nome_universita]["corsi_famosi"].append(nuovo_corso)
        print(f"Corso '{nuovo_corso}' aggiunto all'università {nome_universita}")
    else:
        print(f"L'università '{nome_universita}' non esiste nel dizionario.")


def universita_top(universita):
    top_universita = None
    classifica_min = float(1000)
    
    for nome, info in universita.items():
        if info["classifica_mondiale"] < classifica_min:
            classifica_min = info["classifica_mondiale"]
            top_universita = nome
    
    print(f"L'università più alta in classifica è: {top_universita}")


def elimina_universita(universita, nome_universita):
    if nome_universita in universita:
        del universita[nome_universita]
        print(f"L'università '{nome_universita}' è stata eliminata correttamente")
    else:
        print(f"L'università '{nome_universita}' non esiste nel dizionario.")