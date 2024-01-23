# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro: 
    def __init__(self):
        self.ligado = False
        self.cor = 'Preto'
        self.modeço = 'Corola'
        self.velocidade = 100

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelera(self):
        if not self.ligado:
            return
        
        if self.velocidade < 0:
            self.acelerar += 50

    def desacelera(self):
        if not self.ligado:
            return
        
        if self.velocidade > 100:
            self.desacelera -= 50

    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - acelera {self.velocidade} - desacelera {self.velocidade}'

# Criando instâncias da class Televisao

from televisao import Televisao

tv_sala = Televisao()
tv_sala.ligar()
print('tv_sala está ligada? {}'.format(tv_sala.ligada))

# Crie uma instância da classe carro.

carro = Carro()
carro.ligar()
print('\nO carro está ligado? {}'.format(carro.ligado))

# Faça o carro "andar" utilizando os métodos da sua classe.

carro_acelera = Carro()
carro_acelera.acelera
print('\nO carro está acelerando? {}'.format(carro_acelera.acelera))

# Faça o carro "parar" utilizando os métodos da sua classe.

carro_parou = Carro()
carro_parou.desligar
print('\nO carro está desligado? {}'.format(carro_parou.desligar))