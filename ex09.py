def calcular_media(lista):
    if not lista:
        return None 
    soma = sum(lista)
    media = soma / len(lista)
    return media
numeros = [5, 2, 8, 1, 9, 3, 4, 7, 6]

media = calcular_media(numeros)

if media is not None:
    print("A média dos números é:", media)
else:
    print("A lista está vazia.")
