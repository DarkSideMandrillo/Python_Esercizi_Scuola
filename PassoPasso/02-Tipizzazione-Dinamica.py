# Dichiarazione di una variabile
x = 10  # x è un intero
print(f"x: {x}, tipo: {type(x)}")

# Cambiamo il valore di x
x = "Ciao"  # x diventa una stringa
print(f"x: {x}, tipo: {type(x)}")

# Cambiamo ancora il valore di x
x = [1, 2, 3]  # x diventa una lista
print(f"x: {x}, tipo: {type(x)}")


# -------------------------------------------------------


def incrementa(valore):
    if isinstance(valore, int) or isinstance(valore, float):
        return valore + 1
    elif isinstance(valore, str):
        return valore + " aggiunto"
    else:
        return "Tipo non supportato"


# Test della funzione
print(incrementa(5))  # Restituisce 6
print(incrementa(3.5))  # Restituisce 4.5
print(incrementa("test"))  # Restituisce "test aggiunto"
print(incrementa([1, 2, 3]))  # Restituisce "Tipo non supportato"

# dati = [1, 2, 'Ciao', 3.5, [1, 2], None, 10, 'Mondo', 3.14]
# Crea una funzione che analizza i dati nella lista e li divida in 2 liste:
# stringList e numberList. per aggiungere elementi alla lista bisogna fare .append(elemento)

# -------------------------------------------------------


def analizza_dati(lista):
    numeri = []
    stringhe = []
    for elemento in lista:
        if isinstance(elemento, (int, float)):  # Controllo se è un numero
            numeri.append(elemento)
        elif isinstance(elemento, str):  # Controllo se è una stringa
            stringhe.append(elemento)
    return numeri, stringhe


# Test della funzione
dati = [1, 2, "Ciao", 3.5, [1, 2], None, 10, "Mondo", 3.14]
numeri, stringhe = analizza_dati(dati)
print("Numeri:", numeri)  # Dovrebbe restituire [1, 2, 3.5, 10, 3.14]
print("Stringhe:", stringhe)  # Dovrebbe restituire ['Ciao', 'Mondo']

# -------------------------------------------------------

# scrivere una funzione che accetti una lista di valori di tipi diversi e restituisca:

# Una lista di numeri (interi e float).
# La somma di tutti i numeri.
# La media dei numeri.
