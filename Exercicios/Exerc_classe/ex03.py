class Retangulo:
    def __init__(self, comprimento, largura) -> None:
        self.comprimento = comprimento
        self.largura = largura

    def retornar_valor_lados(self):
        print(f'Comprimento: {self.comprimento}\nLargura: {self.largura}')

    def mudar_valor_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        area = self.comprimento*self.largura
        return area

    def calcular_perimetro(self):
        perimetro = (2*self.comprimento) + (2*self.largura)
        return perimetro


# print('Informe as medidas do local')

# comprimento = input(str('Comprimento: '))
# largura = input(str('Largura: '))
# comprimento = float(comprimento)
# largura = float(largura)
# local = Retangulo(comprimento, largura)
# area_local = local.calcular_area()
# perimetro_local = local.calcular_perimetro()
# lado_piso = 2

# quant_pisos = area_local // (lado_piso**2)
# quant_rodapes = perimetro_local // lado_piso

# print(f'Área do local: {area_local}')
# print(f'Precisrá de {quant_pisos} pisos e {quant_rodapes} rodapés.')
