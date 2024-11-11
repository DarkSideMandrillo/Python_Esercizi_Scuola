def cancellaUniversita(universita, nome):
    del universita[nome]


def addCorso(universita, nome):
    universita[nome]["corsi_famosi"] = universita[nome].add("biotecnologie")
    