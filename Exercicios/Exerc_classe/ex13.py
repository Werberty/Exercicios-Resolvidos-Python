class Funcionario:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario

    def show(self):
        print(f'Nome: {self.nome}\nSalário: R${self.salario:.2f}')
    
    def aumento_de_salario(self, percentual):
        aumento = (percentual/100)*self.salario
        self.salario += aumento


f1 = Funcionario('Thomas', 1000)
f1.aumento_de_salario(20)
f1.show()
