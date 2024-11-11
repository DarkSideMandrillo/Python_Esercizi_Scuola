
def inserisci_corso(nome, corso):
    if nome in universita:
        universita[nome]["corsi_famosi"].append(corso)
        print(f"{corso} aggiunto a {nome}.")
    else:
        print(f"Università {nome} non trovata.")

def universita_top_classifica():
    top_uni = min(universita, key=lambda x: universita[x]["classifica_mondiale"])
    print(f"L'università più alta in classifica è: {top_uni}")

def elimina_universita(nome):
    if nome in universita:
        del universita[nome]
        print(f" {nome} eliminata.")
    else:
        print(f"Università {nome} non trovata.")
