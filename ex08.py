def ordenarLista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

numeros = [5, 2, 8, 1, 9, 3, 4, 7, 6]

listaOrdenada = ordenarLista(numeros)

print("Lista original:", numeros)
print("Lista ordenada:", listaOrdenada)
