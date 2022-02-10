class Carro:
    def __init__(self, consumo) -> None:
        self.consumo = consumo
        self.tanque = 0
    
    def andar(self, distancia):
        if self.tanque == 0:
            print('Tanque vazio...')
            return
        self.tanque -= distancia/self.consumo
    
    def obter_gasolina(self):
        print(f'Nivel do tanque: {self.tanque:.2f}L')
    
    def adicionar_gasolina(self, valor):
        self.tanque += valor
