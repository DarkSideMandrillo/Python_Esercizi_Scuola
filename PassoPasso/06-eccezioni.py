# Try Except
def func0():
    try:
        # Codice che generare un'eccezione
        lista = [1, 2, 3]
        lista[10]
        a = 10
    except:
        # Codice eseguito in eccezione
        print("Errore")


# Catturiamo gli errori
def func1():
    try:
        # Codice che potrebbe generare un'eccezione
        risultato = 10 / 0
    except ZeroDivisionError:
        # Codice eseguito se si verifica un'eccezione di divisione per zero
        print("Non puoi dividere per zero!")


# Si può usare il blocco else: (poco utilizzato)
def func2():
    try:
        risultato = 10 / 2
    except ZeroDivisionError:
        print("Non puoi dividere per zero!")
    else:
        print("Il risultato è:", risultato)


# Generiamo noi un eccezione
def func3():
    try:
        # Genera un'eccezione di tipo ValueError
        raise ValueError("Questo è un messaggio di errore")
    except ValueError as e:
        # Gestisce l'eccezione e stampa il messaggio di errore
        print("Eccezione catturata:", e)


# Finally: viene eseguito anche con eccezione
def func4():
    try:
        file = open("file.txt", "r")
        contenuto = file.read()
    except FileNotFoundError:
        print("Il file non è stato trovato.")
    finally:
        # Chiude il file se è stato aperto
        if "file" in locals():
            file.close()


def main():
    func0()
    func1()
    func2()
    func3()
    func4()


if __name__ == "__main__":
    # Codice da eseguire quando lo script viene eseguito direttamente
    main()
