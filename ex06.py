def contarVogais(string):
    string = string.lower()
    count = 0
    vogais = "aeiou"

    for letra in string:
        if letra in vogais:
            count += 1

    return count


texto = input("Digite uma frase: ")
numeroDeVogais = contarVogais(texto)

print(f"O número de vogais na frase é: {numeroDeVogais}")
