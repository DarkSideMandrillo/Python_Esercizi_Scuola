lista = [50, 45, 30, 20]

# print(lista)
# print(len(lista))

# for i in range(len(lista)):
#     print(lista[i])

# for elemento in lista:
#     print(elemento)

lista = [
    [[1, 2, 3, 7], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12, 21], [3, 4, 11]],
    [[13, 14, 15], [16, 17, 18]],
]


for i in range(len(lista)):
    for j in range(len(lista[i])):
        for k in range(len(lista[j])):
            print(f"Elemento lista posizione [{i}][{j}][{k}]: {lista[i][j][k]}")


for ele1 in lista:
    for ele2 in ele1:
        for ele3 in ele2:
            print(ele3)
