import VerUtil

#---ES1---:

print("!------------------ Esercizio 01 ------------------!")

matrice = []
for i in range(1, 11):
    riga = []
    for j in range(1, 11):
        riga.append(i * j)
    matrice.append(riga)

print("matrice ciclo for:")
print(matrice)


matrice = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print("matrice List Comprehension:")
print(matrice)


#---ES2---:

print("!------------------ Esercizio 02 ------------------!")

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

def inserisci_corso(universita, nome_universita, corso):
    if nome_universita in universita:
        universita[nome_universita]["corsi_famosi"].append(corso)
        print(universita)
    else:
        print("Universita non trovata")

def stampa_universita_migliore(universita):
    universita_migliore = min(universita, key=lambda x: universita[x]["classifica_mondiale"])
    print(universita_migliore)

def elimina_universita(universita, nome_universita):
    if nome_universita in universita:
        del universita[nome_universita]
        print("Università eliminata con successo")
    else:
        print("Università non trovata")

inserisci_corso(universita, "MIT", "MATEMATICA")
stampa_universita_migliore(universita)
elimina_universita(universita, "Università di Oxford")

#---ES3---:

print("!------------------ Esercizio 03 ------------------!")

VerUtil.inserisci_corso(universita, "Politecnico di Milano", "PASTICCERIA")
VerUtil.stampa_universita_migliore(universita)
VerUtil.elimina_universita(universita, "Università di Tokyo")

#---ES4---:


print("!------------------ Esercizio 04 ------------------!")

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

frutta_selezionata = [f for f in frutta if f["calorie"] < 50 or f["peso_g"] < 7]
print(frutta_selezionata)

print("FINE VERIFICA!")

