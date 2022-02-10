class Macaco:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.bucho = 'nada'

    def comer(self, alimento):
        if self.bucho == 'nada':
            self.bucho = alimento
        else:
            print('Ele está cheio')
    
    def ver_bucho(self):
        print(f'{self.nome} tem {self.bucho} no bucho')
    
    def digerir(self):
        self.bucho = 'nada'
