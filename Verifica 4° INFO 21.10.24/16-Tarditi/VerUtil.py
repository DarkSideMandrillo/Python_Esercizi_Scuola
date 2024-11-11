def inserisci_corso(universita, nome_universita, corso):
    if nome_universita in universita:
        universita[nome_universita]["corsi_famosi"].append(corso)
        print(universita)
    else:
        print("Università non trovata")

def stampa_universita_migliore(universita):
    universita_migliore = min(universita, key=lambda x: universita[x]["classifica_mondiale"])
    print(universita_migliore)

def elimina_universita(universita, nome_universita):
    if nome_universita in universita:
        del universita[nome_universita]
        print("Università eliminata con successo")
    else:
        print("Università non trovata")