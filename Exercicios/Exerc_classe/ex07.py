class Tamagushi:
    def __init__(self, nome, fome=10, saude=10, idade=0) -> None:
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar(self, funcao, valor):
        self.idade += 1
        if funcao == 'nome':
            self.nome = valor
        elif funcao == 'saude':
            self.saude = valor
        elif funcao == 'fome':
            self.fome = valor
        elif funcao == 'idade':
            self.idade = valor

    def mostrar(self):
        print(
            f'Nome: {self.nome} \nFome:{self.fome}/10 Saúde:{self.saude}/10 Idade:{self.idade}')
    
    def humor(self):
        h = (self.saude + self.fome) // 2
        print(f'Humor: {h}')
