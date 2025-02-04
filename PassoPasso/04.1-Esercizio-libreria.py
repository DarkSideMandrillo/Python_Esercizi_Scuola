# Scrivi un programma che gestisca una libreria di libri,
# ognuno con le seguenti informazioni:
# titolo, autore e valutazioni (una lista di valutazioni numeriche).
# Il programma dovrà permettere di:

# -Aggiungere un libro alla libreria.
# -Aggiungere una valutazione a un libro esistente.
# -Calcolare e restituire la media delle valutazioni di un libro.
# Mostrare l'elenco di tutti i libri con le loro medie.

# Le funzioni da implementare sono:
# -aggiungi_libro(libreria, titolo, autore) - Aggiunge un nuovo libro al dizionario della libreria.
# -aggiungi_valutazione(libreria, titolo, valutazione) - Aggiunge una valutazione a un libro esistente.
# -calcola_media(libreria, titolo) - Calcola e restituisce la media delle valutazioni di un libro.
# -mostra_libreria(libreria) - Mostra l'elenco di tutti i libri con le loro medie.

# ESEMPIO DEL DIZIONARIO
#     {
# 'Il Signore degli Anelli': {
# 'autore': 'J.R.R. Tolkien',
# 'valutazioni': [5, 4]
# }

dizionarioTest = {}
dizionarioTest["1984"] = {"autore": "orwell", "valutazioni": []}

# In python gli oggetti immutabili vengono passati by value
# tutto il resto byRef


def addBook(library, name, author):
    if name not in library:
        library[name] = {"author": author, "ratings": []}
    else:
        print("Libro già presente")


def addRating(library, name, rating):
    if name in library:
        library[name]["ratings"].append(rating)


def average_book_rating(library, name):
    average = 0
    if len(library[name]["ratings"]) > 0:
        for rating in library[name]["ratings"]:
            average += rating
        average = average / len(library[name]["ratings"])
    return average
    # valutazioni = libreria[titolo]["valutazioni"]
    # return sum(valutazioni) / len(valutazioni) if valutazioni else 0


def show_library(library):
    for key, value in library.items():
        print(f"Titolo: {key} | Media punteggio: {average_book_rating(library,key)}")
    # [print(f"Titolo: {book_name}, Autore: {info['autore']}, Media Valutazioni: {averageBookRating(library, book_name):.2f}") for book_name, info in library.items()]


def main():
    # Codice principale del programma
    library = {}
    addBook(library, "1984", "George Orwell")
    addBook(library, "To Kill a Mockingbird", "Harper Lee")
    addBook(library, "Pride and Prejudice", "Jane Austen")
    addBook(library, "Moby Dick", "Herman Melville")

    addRating(library, "1984", 5)
    addRating(library, "1984", 3)
    addRating(library, "1984", 4)
    addRating(library, "To Kill a Mockingbird", 5)
    addRating(library, "Moby Dick", 3)
    addRating(library, "Moby Dick", 4)
    addRating(library, "Moby Dick", 4)
    addRating(library, "Moby Dick", 4)

    showLibrary(library)


if __name__ == "__main__":
    main()
