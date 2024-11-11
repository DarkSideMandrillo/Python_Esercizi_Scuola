
io = {
    "nome": "tiziano",
    "età": 36,
    "cognome": "meneghetti",
    "altezza": 1.70,
    "peso": 63.0
    }

print(f"io[\"nome\"] {io["nome"]}")
print(f"io[\"età\"] {io.get("età")}")

# crea nuova valore-chiave | cambia un valore di una chiave esistente
io["materia"] = "letteratura"
io["età"] = 26

# Togli una voce
io.pop("altezza")
age=io.pop("età") # storage del valore tolto
lastItem= io.popitem()

del io["nome"]

print(f"age: {age}")
print(f"lastItem: {lastItem}")
print(io)

# Iterarazioni

for key in io:
    print(key)

for value in io.values():
    print(value)
    
for key, value in io.items():
    print(f"{key}: {value}")
    
# Verificare se esiste chiave
if "peso" in io:
    print(f"La chiave peso è presente e vale {io.get("peso")}")
    
print(f"lunghezza io: {len(io)}")
