import csv

with open("vendite.csv", "r") as file:
    listFile = csv.reader(file)
    print(listFile)
    for riga in listFile:
        try:
            nome, cat, qta, prezzo = riga
            print(
                f"Nome: {nome}\nCategoria: {cat}\n   Prezzo Totale: {float(qta)*float(prezzo)}\n-----------\n"
            )
        except:
            print("err")

    # listFile = file.read().splitlines()
    # for riga in listFile:
    #     try:
    #         riga = riga.split(",")
    #         nome_prodotto = riga[0]
    #         categoria = riga[1]
    #         quantita_venduta = riga[2]
    #         prezzo_unitario = riga[3]
    #         print(
    #             f"Nome: {nome_prodotto}\nCategoria: {categoria}\n
    #             Prezzo Totale: {float(quantita_venduta)*float(prezzo_unitario)}\
    #                 n-----------\n"
    #         )
    #     except:
    #         print("Errore riga")
