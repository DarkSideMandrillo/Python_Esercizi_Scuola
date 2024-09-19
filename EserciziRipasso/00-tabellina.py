num = int(input("Inserisci il numero: "))  # input restituisce una stringa
somma = 0

for i in range(10):
    somma += num
    print(f"X*{i}: {somma}")

# range(start, stop, step) lo stop non fa girare
somma = 0
for i in range(3, 31, 3):
    print(i)
