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


Tabellina = [ , , , , , , , , , ,]


for i in range(Tabellina,(Tabellina*10)+1,tabellina):     
    riga = []      
    print(i)

for j in range(Tabellina,(Tabellina*10+1,tabellina)):
      riga.append(i*10*j)
      print(j)

"----------------------------------------------------------------------------"

Tabellina = [i*2 for i in range(10)]
print(Tabellina)





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

  def aggiungi_Univeristà()
    ["Università di Cuneo"] = "italia",1900,700,["Ingegneria","Meccanica", 1]

def stampa_Università():
    
    for i in range Dizionario(Dizionario)
       if Università[0](Classifica_mondiale) < università[i](Classifica_mondiale)
            print(Università(i))

input Università_da_eliminare:
 def delete_Università(Università_da_eliminare)

    del dizionario["Università_da_eliminare"]                       


    
   
  





# ES3
print("!------------------ Esercizio 03 ------------------!")
"""
Crea un nuovo file ("VerUtil.py") in cui COPIARE e incollare le tre funzioni appena create.
Poi riutilizzale con le giuste modifiche
"""




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
    {"nome": "Mela", "calorie": 52, "peso": 150}, 
    {"nome": "Fragola", "calorie": 32, "peso": 5}, 
    {"nome": "Banana", "calorie": 89, "peso": 120},
    {"nome": "Ciliegia", "calorie": 50, "peso": 8}, 
    {"nome": "Melone", "calorie": 34, "peso": 50}, 
    {"nome": "Uva", "calorie": 69, "peso": 100},   
    {"nome": "Lampone", "calorie": 52, "peso": 6},  
]

frutta_leggera = [item for item in frutta if item["calorie"] < 50 or item["peso"] < 7]

print(frutta_leggera)











	Valutazione

Esercizio 1
3
Esercizio 2
3
Esercizio 3
2
Esercizio 4
2
Clean code
2




