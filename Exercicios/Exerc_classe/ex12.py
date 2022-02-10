class ContaDeInvestimento:
    def __init__(self, saldo_inicial, taxa_inicial) -> None:
        self.saldo_inicial = saldo_inicial
        self.taxa_inicial = taxa_inicial
    
    def adiciona_juros(self):
        self.saldo_inicial += (self.taxa_inicial/100)*self.saldo_inicial
