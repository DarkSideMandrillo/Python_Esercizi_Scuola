def NuovoCorso(dizionario,nome,dati):
    dizionario[nome] = dati
    
def UniversitaPrimaInClassifica(dizionario):
    name=""
    max = 0
    for k,v in dizionario.items():
        if(max==0):
            max=v["classifica_mondiale"]
            name = k
        if(max>v["classifica_mondiale"]):
            name = k
            max=v["classifica_mondiale"]
    return name,max

def EliminaUniversita(dizionario,nome):
    dizionario.pop(nome)