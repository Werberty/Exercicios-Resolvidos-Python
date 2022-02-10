class Tv:
    def __init__(self) -> None:
        self.canal = 0
        self.volume = 5
        self.range_canais = list(range(0, 21))

    def mudar_canal(self, canal):
        if canal in self.range_canais:
            self.canal = canal
        print(f'CH {self.canal}')
    
    def aumentar_volume(self):
        if self.volume >= 10:
            return
        self.volume += 1
        print(f'Vol {self.volume}')
    
    def diminuir_volume(self):
        if self.volume <= 0:
            return
        self.volume -= 1
