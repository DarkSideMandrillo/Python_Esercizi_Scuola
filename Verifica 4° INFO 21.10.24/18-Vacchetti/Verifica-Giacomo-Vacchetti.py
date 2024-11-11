import VerUtil


print("!------------------ Esercizio 01 ------------------!")

list = [[i*j for i in range(1,11)] for j in range(1,11)]
print(list)
list=[]

print("!------------------ No list Comprension ------------------!")
for i in range (1,11):
    tabellina =[]
    for j in range(1,11):
        tabellina.append(i*j)
    list.append(tabellina)
print(list)
    
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

def NuovoCorso(nome,dati):
    universita[nome] = dati
    
def UniversitaPrimaInClassifica():
    name=""
    max = 0
    for k,v in universita.items():
        if(max==0):
            max=v["classifica_mondiale"]
            name = k
        if(max>v["classifica_mondiale"]):
            name = k
            max=v["classifica_mondiale"]
    return name,max

def EliminaUniversita(nome):
    universita.pop(nome)

print("!------------------ aggiunta universita di torino------------------!")
NuovoCorso("!------------------ Università di Torino",{
        "paese": "Italia",
        "anno_fondazione": 1923,
        "numero_studenti": 13000,
        "corsi_famosi": ["Ingegneria", "Scienze della Vita", "Economia"],
        "classifica_mondiale": 24
    })
print(universita)
EliminaUniversita("!------------------ Università di Torino------------------!")
print("!------------------ eliminata universita di torino------------------!")
print(universita)
print("!------------------ universita più alta in classifica------------------!")
print(UniversitaPrimaInClassifica())

print("!------------------ Esercizio 03 ------------------!")
print("!------------------ aggiunto universita di mosca------------------!")
VerUtil.NuovoCorso(universita,"Università di Mosca",{
        "paese": "Russia",
        "anno_fondazione": 1823,
        "numero_studenti": 16000,
        "corsi_famosi": ["Ingegneria", "Scienze della Vita", "Economia"],
        "classifica_mondiale": 49
    })
print(universita)
VerUtil.EliminaUniversita(universita,"Università di Mosca------------------!")
print("!------------------ eliminato universita di mosca------------------!")
print(universita)
print("!------------------ Università più alta in classifica------------------!")
print(VerUtil.UniversitaPrimaInClassifica(universita))


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

list = [i for i in frutta if i["peso_g"]<7 or i["calorie"]<50]
print("!------------------ lista con meno di 7g o meno di 50 calorie------------------!")
print(list)