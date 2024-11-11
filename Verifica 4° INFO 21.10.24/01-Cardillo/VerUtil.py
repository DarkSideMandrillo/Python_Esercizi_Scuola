def aggiungiCorso(universita, nome, corso):
    valoreUni = universita[nome]
    corsi = valoreUni["corsi_famosi"]
    corsi.append(corso) 

def eliminaUni(universita, nome):
    del universita[nome]