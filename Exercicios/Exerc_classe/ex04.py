class Pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(aumento=0.05)

    def engordar(self):
        self.peso += 2

    def emagrecer(self):
        self.peso -= 2

    def crescer(self, aumento=0.1):
        self.altura += aumento
