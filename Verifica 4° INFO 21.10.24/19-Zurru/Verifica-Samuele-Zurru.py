# Crea un file "verifica-nome-cognome.py" e incolla il seguente testo/codice

# ES1
print("!------------------ Esercizio 01 ------------------!")
"""
Crea una matrice 10*10 che rappresenti le tabelline
[
    [1,2,3,4,5,6,7,8,9,10],
    [2,4,6,8,10,12,14,16,18,20],
    [3,6,9,12,15,18,21,24,27,30],
    ...
]
Esegui l'esercizio sia con il ciclo FOR che con il List Comprehension
"""
    
matrice = []


for i in range(1, 11):
   
    riga = []
   
    for j in range(1, 11):
   
        riga.append(i * j)
   
    matrice.append(riga)


for riga in matrice:
    print(riga)
    
# Creazione della matrice con list comprehension
matrice = [[i * j for j in range(1, 11)] for i in range(1, 11)]


for riga in matrice:
    print(riga)
  
      

# ES2
print("!------------------ Esercizio 02 ------------------!")
"""
Partendo da questo dizionario:

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

Crea tre funzioni: (no list comprehension)
1) Inserisci una nuovo corso ad una università presa in input
2) Stampa il nome dell'università più alta in classifica
3) Elimina una università presa in input
"""
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





# ES3
print("!------------------ Esercizio 03 ------------------!")
"""
Crea un nuovo file ("VerUtil.py") in cui COPIARE e incollare le tre funzioni appena create.
Poi riutilizzale con le giuste modifiche
"""
from VerUtil import  inserisci_corso(),universita_piu_alta(),elimina_universita()


# ES4
print("!------------------ Esercizio 04 ------------------!")
"""
Dato questo dizionario:

frutta = [
    {
        "nome": "Mela",
        "colore": "Rosso",
        "peso_g": 150,
        "calorie": 52,
        "vitamina_C_mg": 4.6
    },
    {
        "nome": "Banana",
        "colore": "Giallo",
        "peso_g": 120,
        "calorie": 89,
        "vitamina_C_mg": 8.7
    },
    {
        "nome": "Arancia",
        "colore": "Arancione",
        "peso_g": 130,
        "calorie": 47,
        "vitamina_C_mg": 53.2
    },
    {
        "nome": "Fragola",
        "colore": "Rosso",
        "peso_g": 12,
        "calorie": 32,
        "vitamina_C_mg": 58.8
    },
    {
        "nome": "Uva",
        "colore": "Verde/Rosso",
        "peso_g": 5,
        "calorie": 69,
        "vitamina_C_mg": 10.8
    }
]



Crea una lista di dizionari contenente solo la frutta che ha meno di 50 calorie
o che pesa meno di 7g. Usa una List Comprehension
"""
frutta = [
    {
        "nome": "Mela",
        "colore": "Rosso",
        "peso_g": 150,
        "calorie": 52,
        "vitamina_C_mg": 4.6
    },
    {
        "nome": "Banana",
        "colore": "Giallo",
        "peso_g": 120,
        "calorie": 89,
        "vitamina_C_mg": 8.7
    },
    {
        "nome": "Arancia",
        "colore": "Arancione",
        "peso_g": 130,
        "calorie": 47,
        "vitamina_C_mg": 53.2
    },
    {
        "nome": "Fragola",
        "colore": "Rosso",
        "peso_g": 12,
        "calorie": 32,
        "vitamina_C_mg": 58.8
    },
    {
        "nome": "Uva",
        "colore": "Verde/Rosso",
        "peso_g": 5,
        "calorie": 69,
        "vitamina_C_mg": 10.8
    }
]


frutta_leggera = [f for f in frutta if f["calorie"] < 50 or f["peso_g"] < 7]


print(frutta_leggera)