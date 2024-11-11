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