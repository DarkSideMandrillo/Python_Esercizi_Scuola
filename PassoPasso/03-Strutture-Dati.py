from collections import Counter


# Una raccolta ordinata e modificabile di elementi. Permette duplicati.
animali = ["cane", "gatto", "coniglio", "cavallo", "pappagallo"]
terzo_animale = animali[2]  # Terzo elemento
animali.append("tartaruga")  # Aggiungi un nuovo nome
lista_aggiornata = animali  # Lista aggiornata

# ------------------ TUPLE ---------------------- #
# Una raccolta ordinata e immutabile di elementi. Permette duplicati.
colori = ("rosso", "verde", "blu")
primo_colore = colori[0]  # Primo colore
# Modifica non possibile:
# colori[1] = "giallo"  # Questo genererà un errore

# ------------------ SET ---------------------- #
# Una raccolta non ordinata di elementi unici. Non permette duplicati.
numeri = {1, 2, 3, 4, 5}
set_iniziale = numeri  # Stampa il set iniziale
numeri.add(6)  # Aggiungi un numero
set_aggiornato = numeri  # Set aggiornato

# ------------------ DICT ---------------------- #
# Una raccolta non ordinata di coppie chiave-valore. Le chiavi sono uniche. Da Py3.7 è ordinata
dizionario = {"nome": "Mario", "età": 30}
valore_nome = dizionario["nome"]  # Valore associato alla chiave "nome"
dizionario["città"] = "Roma"  # Aggiungi nuova coppia
del dizionario["città"]  # Rimuove la chiave "città"
eta = dizionario.pop("età")  # Rimuove e restituisce il valore associato a "professione"
dizionario.get(
    "nome", "non trovato"
)  # è come il dizionario["nome"] ma gestisce il non trovato
dizionario_aggiornato = dizionario  # Dizionario aggiornato

for chiave in dizionario:
    print(chiave, dizionario[chiave])  # Stampa ciascuna chiave e il suo valore

# Oppure per ottenere le coppie chiave-valore
for chiave, valore in dizionario.items():
    print(chiave, valore)

# len(dizionario): Restituisce il numero di elementi nel dizionario.
# dizionario.keys(): Restituisce un oggetto vista delle chiavi.
# dizionario.values(): Restituisce un oggetto vista dei valori.
# dizionario.items(): Restituisce un oggetto vista delle coppie chiave-valore.

# ------------------ STRING ---------------------- #
# Una sequenza di caratteri. Le stringhe sono immutabili.
frase = "Ciao, come va?"
lunghezza_stringa = len(frase)  # Lunghezza della stringa
stringa_modificata = frase.replace("Ciao", "Salve")  # Sostituisci una parola

# ------------------ COUNTER ---------------------- #
# Una sequenza di caratteri. Le stringhe sono immutabili.
lettere_counter = Counter("hello world")  # Contare la frequenza delle lettere
frutti = ["mela", "banana", "mela", "pera", "banana", "banana"]
frutti_counter = Counter(frutti)  # Creare un Counter per la lista di frutti


# Stampa dei risultati
print("Esercizio LIST:")
print("Terzo animale:", terzo_animale)
print("Lista aggiornata:", lista_aggiornata)

print("\nEsercizio TUPLE:")
print("Primo colore:", primo_colore)

print("\nEsercizio SET:")
print("Set iniziale:", set_iniziale)
print("Set aggiornato:", set_aggiornato)

print("\nEsercizio DICT:")
print("Valore nome:", valore_nome)
print("Dizionario aggiornato:", dizionario_aggiornato)

print("\nEsercizio STRING:")
print("Lunghezza stringa:", lunghezza_stringa)
print("Stringa modificata:", stringa_modificata)

print("\nEsercizio COUNTER:")
print("Frequenza lettere:", lettere_counter)
print("Frequenza frutti:", frutti_counter)
