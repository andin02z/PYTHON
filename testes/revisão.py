class Televisao:
    def _init_(self, tamanho, canal):
        self.tamanho = tamanho
        self.canal = canal
        self.ligada = False

    def get_tamanho(self):
        return self.tamanho
    
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        return self.tamanho
    
    def get_canal(self):
        return self.canal
    
    def set_canal(self, muda_canal):
        self.canal = muda_canal
        return self.canal
    
    def ligar(self):
        self.ligada = True
        return self.ligada
    
    def desligar(self):
        self.ligada = False
        return self.ligada
    
    def _str_(self):
        return f'O tamanho da Televisão é {self.get_tamanho()}, está no canal {self.get_canal()}. A Televisão está ligada? {self.ligada}'

tv = Televisao('32 polegadas', 1)

print(tv)