class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel) -> None:
        self._tipo_combustivel = tipo_combustivel
        self._valor_litro = valor_litro
        self._quantidade_combustivel = quantidade_combustivel
    
    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self, valor):
        self._tipo_combustivel = valor
    
    @property
    def valor_litro(self):
        return self._valor_litro
    
    @valor_litro.setter
    def valor_litro(self, valor):
        self._valor_litro = valor
    
    @property
    def quantidade_combustivel(self):
        return self._quantidade_combustivel
    
    @quantidade_combustivel.setter
    def quantidade_combustivel(self, valor):
        self._quantidade_combustivel = valor
    
    def mostrar_bomba(self):
        print(f"""
Tipo de combustivel: {self.tipo_combustivel}
Valor do litro: R$ {self.valor_litro:.2f}
Qauntidade combsutivel na bomba: {self.quantidade_combustivel:.2f}
""")

    def abastecer_por_valor(self, valor):
        quatidade = valor/self.valor_litro
        self.quantidade_combustivel -= quatidade

    def abastecer_por_litro(self, litros):
        self.quantidade_combustivel -= litros

    def alterar_valor(self, valor):
        self.valor_litro = valor

    def alterar_combustivel(self, tipo):
        self.tipo_combustivel = tipo

    def alterar_quantidade_combustivel(self, valor):
        self.quantidade_combustivel = valor
