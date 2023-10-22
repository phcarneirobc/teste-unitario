def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

lista = [5, -3, 7, 0, -2, 9, -1]

resultado = somar_lista(lista)

print(f"A soma dos elementos da lista é: {resultado}")
