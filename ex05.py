class ContaBancária:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"
        else:
            return "Valor de depósito inválido."

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"
        elif valor <= 0:
            return "Valor de saque inválido."
        else:
            return "Saldo insuficiente."

    def get_saldo(self):
        return self.saldo

minha_conta = ContaBancária(1000)

while True:
    print("\nEscolha uma operação:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Saldo")
    print("4. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
        valor = float(input("Digite o valor do depósito: "))
        print(minha_conta.deposito(valor))
    elif escolha == '2':
        valor = float(input("Digite o valor do saque: "))
        print(minha_conta.saque(valor))
    elif escolha == '3':
        print(f"Saldo atual: R${minha_conta.get_saldo()}")
    elif escolha == '4':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")
