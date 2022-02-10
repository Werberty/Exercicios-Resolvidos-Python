class Retangulo:
    def __init__(self, largura, altura) -> None:
        self.largura = largura
        self.altura = altura
        self.ponto = Ponto()
    
    def encontrar_centro(self):
        xc = self.largura / 2
        yc = self.altura / 2
        self.ponto.x = xc
        self.ponto.y = yc


class Ponto:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def imprime_valores(self):
        print(f'X:{self.x} Y:{self.y}')
