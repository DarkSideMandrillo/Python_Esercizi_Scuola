universita = {
    "MIT": {
        "paese": "USA",
        "anno_fondazione": 1861,
        "numero_studenti": 11500,
        "corsi_famosi": ["Informatica", "Ingegneria", "Fisica"],
        "classifica_mondiale": 1
    },
    "Università di Oxford": {
        "paese": "Regno Unito",
        "anno_fondazione": 1096,
        "numero_studenti": 24000,
        "corsi_famosi": ["Filosofia", "Legge", "Economia"],
        "classifica_mondiale": 2
    },
    "Università di Tokyo": {
        "paese": "Giappone",
        "anno_fondazione": 1877,
        "numero_studenti": 28000,
        "corsi_famosi": ["Ingegneria", "Scienze della Vita", "Economia"],
        "classifica_mondiale": 23
    },
    "Politecnico di Milano": {
        "paese": "Italia",
        "anno_fondazione": 1863,
        "numero_studenti": 42000,
        "corsi_famosi": ["Architettura", "Ingegneria Meccanica", "Design"],
        "classifica_mondiale": 137
    }
}

def inserisci_corso(nome_universita, nuovo_corso):
    print("\n---'inserisci_corso' di VerUtil.py---")
    if nome_universita in universita:
        universita[nome_universita]["corsi_famosi"].append(nuovo_corso)
        print(f"Corso '{nuovo_corso}' aggiunto a {nome_universita}.")
    else:
        print(f"Università '{nome_universita}' non trovata.")

def universita_top_classifica():
    print("\n---'universita_top_classifica' di VerUtil.py---")
    top_universita = None
    top_classifica = float('inf')
    
    for nome, dettagli in universita.items():
        if dettagli["classifica_mondiale"] < top_classifica:
            top_classifica = dettagli["classifica_mondiale"]
            top_universita = nome
    
    if top_universita:
        print(f"L'università più alta in classifica è: {top_universita}")
    else:
        print("Nessuna università trovata.")

def elimina_universita(nome_universita):
    print("\n---'elimina_universita' di VerUtil.py---")
    if nome_universita in universita:
        del universita[nome_universita]
        print(f"Università '{nome_universita}' eliminata.")
    else:
        print(f"Università '{nome_universita}' non trovata.")


def funzioni_verutil():
    inserisci_corso("Università di Tokyo", "Astronomia")
    universita_top_classifica()
    elimina_universita("Università di Oxford")