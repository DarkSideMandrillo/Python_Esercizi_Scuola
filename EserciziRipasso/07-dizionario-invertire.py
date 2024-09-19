dizionario = {"a": 1, "b": 2, "c": 3}
dizionarioInvertito = {}

for key, value in dizionario.items():
    dizionarioInvertito[value] = key

print(dizionarioInvertito)

dizionario = {"a": 1, "b": 2, "c": 3}
dizionario_invertito = {v: k for k, v in dizionario.items()}
print(dizionario_invertito)
