class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente")

    def verificar_saldo(self):
        print(f"Saldo atual da conta de {self.nome}: R${self.saldo}")

class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        if conta.nome not in self.contas:
            self.contas[conta.nome] = conta
            print(f"Conta de {conta.nome} criada com sucesso")
        else:
            print("Nome de conta já existente. Por favor, escolha outro nome")

    def realizar_deposito(self, nome, valor):
        if nome in self.contas:
            self.contas[nome].depositar(valor)
        else:
            print("Conta não encontrada")

    def realizar_saque(self, nome, valor):
        if nome in self.contas:
            self.contas[nome].sacar(valor)
        else:
            print("Conta não encontrada")

    def verificar_saldo(self, nome):
        if nome in self.contas:
            self.contas[nome].verificar_saldo()

banco = Banco()

#Criando contas
conta1 = ContaBancaria("João")
conta2 = ContaBancaria("Maria")

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

#Operações bancárias
banco.realizar_deposito("João", 1000)
banco.realizar_deposito("Maria", 500)
banco.realizar_saque("João", 200)
banco.verificar_saldo("João")
