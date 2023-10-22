def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = numero1 + numero2
        operacao = 'adição'
    elif escolha == '2':
        resultado = numero1 - numero2
        operacao = 'subtração'
    elif escolha == '3':
        resultado = numero1 * numero2
        operacao = 'multiplicação'
    elif escolha == '4':
        if numero2 == 0:
            return "Erro! Não é possível dividir por zero."
        resultado = numero1 / numero2
        operacao = 'divisão'
    else:
        return "Opção inválida"

    return f"O resultado da {operacao} de {numero1} e {numero2} é: {resultado}"
print(calculadora())
