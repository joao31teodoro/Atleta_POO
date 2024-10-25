from atletas import *

class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self):
        info = self.aquecer()
        info += self.nadar()
        info += self.pedalar()
        info += self.correr()
        return info

if __name__ == "__main__":
    bolt = Triatleta('Usain Bolt', 38, 86.2)
    print(bolt.realizar_maratona())