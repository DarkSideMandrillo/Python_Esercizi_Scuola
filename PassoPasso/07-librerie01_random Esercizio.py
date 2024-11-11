import random

giocatori = ["mario", "giovanni", "giorgio", "alessio"]

ordine_turno = random.shuffle(giocatori)
primo_giocatore = random.randint(1, 4)

print("Il primo giocatore è", giocatori[primo_giocatore])


# turno_uno {giocatori[primo_giocatore] = }
