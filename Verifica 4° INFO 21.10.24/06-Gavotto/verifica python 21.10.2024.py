# ES1
print("!------------------ Esercizio 01 ------------------!")
#
#Esegui l'esercizio sia con il ciclo FOR che con il List Comprehension

#SOLUZIONE ES1

# Soluzione con ciclo FOR
def matrice_tabelline_for():
    tabellina = []
    for i in range(1, 11):
        riga = []; 
        for j in range(1, 11):
            riga.append(i * j)
            tabellina.append(riga)

    for riga in tabellina:
        print(riga)

# Soluzione con List Comprehension
def matrice_tabelline_listC():
    tabellina_compr = [[i * j for j in range(1, 11)] for i in range(1, 11)]
    print(tabellina_compr)


# ES2
print("!------------------ Esercizio 02 ------------------!")
#
#
#Crea tre funzioni: (no list comprehension)
#1) Inserisci una nuovo corso ad una università presa in input
#2) Stampa il nome dell'università più alta in classifica
#3) Elimina una università presa in input

# SOLUZIONE ES2

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
    print("inserire nome universita a cui aggiungere un corso:")
    nome = input()
    print("inserire corso da aggiungere")
    corso = input()
    
    if nome in universita:
        universita[nome]["corsi_famosi"].append(corso)
        print(f"{corso} aggiunto a {nome}.")
    else:
        print(f"Università {nome} non trovata.")

def universita_top_classifica():
    top_uni = min(universita, key=lambda x: universita[x]["classifica_mondiale"])
    print(f"L'università più alta in classifica è: {top_uni}")

def elimina_universita():
    print("inserire nome universita da eliminare:")
    nome = input()
    if nome in universita:
        del universita[nome]
        print(f" {nome} eliminata.")
    else:
        print(f"Università {nome} non trovata.")


# ES3
print("!------------------ Esercizio 03 ------------------!")
#"""
#Crea un nuovo file ("VerUtil.py") in cui COPIARE e incollare le tre funzioni appena create.
#Poi riutilizzale con le giuste modifiche

# ES4
print("!------------------ Esercizio 04 ------------------!")
#"""

#Crea una lista di dizionari contenente solo la frutta che ha meno di 50 calorie
#o che pesa meno di 7g. Usa una List Comprehension

#SOLUZIONE ES4


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

def filtra_frutta():
    frutta_filtrata = [frutto for frutto in frutta if frutto["calorie"] < 50 or frutto["peso_g"] < 7]
    print(frutta_filtrata)

def main():
    matrice_tabelline_for()
    




def main():
    
    matrice_tabelline_for()
    
    matrice_tabelline_listC()
    
    inserisci_corso()
    
    universita_top_classifica()
    
    elimina_universita()
    
    filtra_frutta()
    
if __name__ == "__main__":
    main()
