# ES1
print("!------------------ Esercizio 01 ------------------!")

#Crea una matrice 10*10 che rappresenti le tabelline
#[
#    [1,2,3,4,5,6,7,8,9,10],
#    [2,4,6,8,10,12,14,16,18,20],
#    [3,6,9,12,15,18,21,24,27,30],
#    ...
#]
#Esegui l'esercizio sia con il ciclo FOR che con il List Comprehension


matrice = []
for i in range(11):
    for j in range(11):
        Matrice = [i*j]
           
        print(matrice)



#matrice2 = [[for i in range(10)] for j in range(10)]
#print(matrice2)





# ES2
print("!------------------ Esercizio 02 ------------------!")

#Partendo da questo dizionario:


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


#Crea tre funzioni: (no list comprehension)
#1) Inserisci una nuovo corso ad una università presa in input
#2) Stampa il nome dell'università più alta in classifica
#3) Elimina una università presa in input

def addUni(nome, paese, annoFondazione, numeroStudenti, corsiFamosi, classifica):
    universita[nome] = {"paese":paese, 
                        "anno_fondazione":annoFondazione, 
                        "numero_studenti": numeroStudenti, 
                        "corsi_famosi":corsiFamosi, 
                        "classifica_mondiale": classifica}
    

def trovaMiglioreUni():
    classMax = 0
    for i in range(universita):
        if (universita["classifica_mondiale"] > classMax):
            classMax += universita["classifica_mondiale"]
    print(classMax)

def deleteUni(nome):
    for i in range(universita):
        if(universita["nome"] == nome):
            universita.clear[i]




# ES3

print("!------------------ Esercizio 03 ------------------!")

#Crea un nuovo file ("VerUtil.py") in cui COPIARE e incollare le tre funzioni appena create.
#Poi riutilizzale con le giuste modifiche

import VerUtil as vu

vu.addUni
vu.trovaMiglioreUni
vu.deleteUni



# ES4
print("!------------------ Esercizio 04 ------------------!")

#Dato questo dizionario:

frutti = [
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

fruttaLeggera = [{frutta}for frutta in frutti where frutti["calorie"] < 50 or frutti["peso_g"] < 7]



#Crea una lista di dizionari contenente solo la frutta che ha meno di 50 calorie
#o che pesa meno di 7g. Usa una List Comprehension
