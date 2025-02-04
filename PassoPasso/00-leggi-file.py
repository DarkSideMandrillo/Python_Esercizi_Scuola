def main():

    file = open("temp.csv", "r")

    temp = file.read().splitlines()
    print(temp)
    print("\n-------------------------\n")
    temp = [element.split(",") for element in temp]
    # [print(element) for element in temp]

    dizionario = {
        chiave: [riga[1:] for riga in temp if riga[0] == chiave]
        for chiave in set(riga[0] for riga in temp)
    }

    # Stampa del risultato
    print(dizionario)

    file.close()


if __name__ == "__main__":
    main()
