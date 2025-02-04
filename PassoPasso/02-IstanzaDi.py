# # Dichiarazione di una variabile
# x = 10  # x è un intero
# print(f"x: {x}, tipo: {type(x)}")

# # Cambiamo il valore di x
# x = "Ciao"  # x diventa una stringa
# print(f"x: {x}, tipo: {type(x)}")

# # Cambiamo ancora il valore di x
# x = [1, 2, 3]  # x diventa una lista
# print(f"x: {x}, tipo: {type(x)}")

# ----------------------------------------------------


def controllo(valore):
    print(isinstance(valore, float))


controllo(1.5)

a = 10
b = 5
c = 3

if a > b:
    print("")
elif a > c:
    print("")
else:
    print("")


def incrementa(valore):
    if isinstance(valore, int) or isinstance(valore, float):
        return valore + 1
    elif isinstance(valore, str):
        return valore + " aggiunto"
    else:
        return "Tipo non supportato"


print(incrementa(5))
print(incrementa(3.5))
print(incrementa("ciao"))


# 6
# 4.5
# text ciao
