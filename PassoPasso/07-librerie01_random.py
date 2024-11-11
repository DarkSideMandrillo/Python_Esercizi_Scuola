import random

print(random.random())  # Output: un numero casuale tra 0.0 e 1.0

print(random.randint(1, 10))  # Output: un numero intero tra 1 e 10

colors = ['red', 'green', 'blue']
print(random.choice(colors))  # Output: Elemento casuale della lista

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)  # Output: la lista mescolata

print(random.uniform(1.5, 3.5))  # Output: un numero decimale tra 1.5 e 3.5



# Esercizio

# Simula il lancio di un dado a 6 facce
def roll_dice():
    return random.randint(1, 6)

# Estrai un elemento a caso da una lista di giocatori
players = ['Alice', 'Bob', 'Charlie', 'David']
first_player = random.choice(players)

# Mescola l'ordine dei giocatori
random.shuffle(players)

print("L'ordine dei giocatori è:", players)
print("Il primo giocatore è:", first_player)
print(f"{first_player} Lancia il dado:", roll_dice())
