class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo=0) -> None:
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def mostra_saldo(self):
        print(f'Titular: {self.nome}')
        print(f'Saldo = R$ {self.saldo:.2f}')
