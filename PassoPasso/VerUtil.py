# 1
def inserimento_nuovo_corso(nome_universita, dizionario):
    if nome_universita in dizionario.keys():
        nuovo_corso = input("Inserisci il nome del nuovo corso: ")
        dizionario[nome_universita]["corsi_famosi"].append(nuovo_corso)


# 2
def migliore_classifica(dizionario):
    classifica = 99999
    for uniNome, uniDati in dizionario.items():
        if uniDati["classifica_mondiale"] < classifica:
            classifica = uniDati["classifica_mondiale"]
            best = uniNome
    print(best)


# 3
def cancellaUniversita(nome_universita, dizionario):
    if nome_universita in dizionario:
        del dizionario[nome_universita]
