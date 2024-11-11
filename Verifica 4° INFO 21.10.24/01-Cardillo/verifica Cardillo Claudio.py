import VerUtil


print("!------------------ Esercizio 01 ------------------!")

# tabellina = [10][10]

# for i in tabellina:
#    for j in tabellina[i]:
#         tabellina[i] = [x * j for x in range(10)]


print("!------------------ Esercizio 02 ------------------!")

universita = {
    "MIT": {
        "paese": "USA",
        "anno_fondazione": 1861,
        "numero_studenti": 11500,
        "corsi_famosi": ["Informatica", "Ingegneria", "Fisica"],
        "classifica_mondiale": 1,
    },
    "Università di Oxford": {
        "paese": "Regno Unito",
        "anno_fondazione": 1096,
        "numero_studenti": 24000,
        "corsi_famosi": ["Filosofia", "Legge", "Economia"],
        "classifica_mondiale": 2,
    },
    "Università di Tokyo": {
        "paese": "Giappone",
        "anno_fondazione": 1877,
        "numero_studenti": 28000,
        "corsi_famosi": ["Ingegneria", "Scienze della Vita", "Economia"],
        "classifica_mondiale": 23,
    },
    "Politecnico di Milano": {
        "paese": "Italia",
        "anno_fondazione": 1863,
        "numero_studenti": 42000,
        "corsi_famosi": ["Architettura", "Ingegneria Meccanica", "Design"],
        "classifica_mondiale": 137,
    },
}


VerUtil.aggiungiCorso(universita, "MIT", "poplpo")
VerUtil.eliminaUni(universita, "Politecnico di Milano")


# ES4
print("!------------------ Esercizio 04 ------------------!")
# Dato questo dizionario:

frutta = [
    {
        "nome": "Mela",
        "colore": "Rosso",
        "peso_g": 150,
        "calorie": 52,
        "vitamina_C_mg": 4.6,
    },
    {
        "nome": "Banana",
        "colore": "Giallo",
        "peso_g": 120,
        "calorie": 89,
        "vitamina_C_mg": 8.7,
    },
    {
        "nome": "Arancia",
        "colore": "Arancione",
        "peso_g": 130,
        "calorie": 47,
        "vitamina_C_mg": 53.2,
    },
    {
        "nome": "Fragola",
        "colore": "Rosso",
        "peso_g": 12,
        "calorie": 32,
        "vitamina_C_mg": 58.8,
    },
    {
        "nome": "Uva",
        "colore": "Verde/Rosso",
        "peso_g": 5,
        "calorie": 69,
        "vitamina_C_mg": 10.8,
    },
]

# Crea una lista di dizionari contenente solo la frutta che ha meno di 50 calorie
# o che pesa meno di 7g. Usa una List Comprehension

prodotti_salutari = [
    frutto for frutto in frutta if frutto["calorie"] < 50 or frutto["peso_g"] < 7
]
print(prodotti_salutari)
