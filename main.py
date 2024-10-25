from atletas import *

if __name__ == "__main__":
    bolt = Corredor('Usain Bolt', 38, 86.2)
    print(bolt)
    print(bolt.aquecer())
    print(bolt.correr())

    cielo = Nadador('Cesar Cielo', 37, 88.8)
    print(cielo)
    print(cielo.aquecer())
    print(cielo.nadar())

    avacini = Ciclista('Henrique Avacini', 35, 67.2)
    print(avacini)
    print(avacini.aquecer())
    print(avacini.pedalar())

    keller = Triatleta('Fernando Keller', 64, 56.5)
    print(keller)
    print(keller.realizar_maratona())