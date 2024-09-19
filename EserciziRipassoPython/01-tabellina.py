# Tabellina del ?
# L'input restituisce una stringa, devo trasformarla in INT
numTabellina = int(input("Inserisci il numero della tabellina: "))

# range(inizio,fine,step)
for i in range(numTabellina, (numTabellina * 10) + 1, numTabellina):
    print(i)
