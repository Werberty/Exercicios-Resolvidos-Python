
class Quadrado:
    def __init__(self, tamanho_do_lado) -> None:
        self.tamanho_do_lado = tamanho_do_lado

    def retornar_valor_lado(self):
        return self.tamanho_do_lado

    def mudar_valor_lado(self, novo_valor):
        self.tamanho_do_lado = novo_valor

    def calcular_area(self):
        area = self.tamanho_do_lado*self.tamanho_do_lado
        print(f'Área: {area}')
