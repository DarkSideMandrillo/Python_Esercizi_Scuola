factorial = 1
numInput = int(input("insert number for factorialize: "))

while numInput != 0:
    factorial *= numInput
    numInput -= 1

print(f"Il fattoriale è {factorial}")

n = int(input("Inserisci un numero: "))
fattoriale = 1
i = 1
while i <= n:
    fattoriale *= i
    i += 1
print(f"Il fattoriale di {n} è {fattoriale}")
