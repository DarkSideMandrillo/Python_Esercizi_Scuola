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

# 1) Inserisci una nuovo corso ad una università presa in input
def aggiungiCorso(nomeUniversita):
    for key, value in universita.items():
        if(nomeUniversita==key):
            value["corsi_famosi"].append("Economia e Management")
    return nomeUniversita, universita[nomeUniversita]

# 2) Stampa il nome dell'università più alta in classifica
def miglioreInClassifica():
    posizione_migliore = 200
    for key, value in universita.items():
        posizione_specifica = value["classifica_mondiale"]
        if(posizione_specifica<posizione_migliore):
            posizione_migliore = posizione_specifica
    return posizione_migliore
print(f"\nPosizione migliore: {miglioreInClassifica()}")

# 3) Elimina una università presa in input
def eliminaUniversita(nome):
    try:
        for key, value in universita.items():
            if(key==nome):
                del universita[nome]
        return universita
    except: print("L'università non esiste")