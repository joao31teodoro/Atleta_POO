from abc import ABC, abstractmethod

class Atleta(ABC):
    nome : str
    idade : int
    peso : float

    def __init__(self, n: str, i: int, p: float):
        self.nome = n
        self.idade = i
        self.peso = p

    def aquecer(self):
        return "Aquecendo..."

    def __str__(self):
        info = f'Nome: {self.nome}, '
        info += f'{self.idade} anos, '
        info += f'{self.peso:2f} Kg'
        return info

class Corredor(Atleta):
    def correr(self):
        return "Correndo..."

class Nadador(Atleta):
    def nadar(self):
        return "Nadando..."

class Ciclista(Atleta):
    def pedalar(self):
        return "Pedalando..."

class Triatleta(Nadador, Ciclista, Corredor):
    def realizar_maratona(self):
        info = self.aquecer()
        info += self.nadar()
        info += self.pedalar()
        info += self.correr()
        return info