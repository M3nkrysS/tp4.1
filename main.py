"""
Lucas B.T.
Gr: 401
introduction à POOP
"""
import random
from math import pi


class StringFoo:
    def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message.upper())


class Rectangle:
    def __init__(self, length, width, ):
        self.length = length
        self.width = width

    def calcul_aire(self):
        self.aire = self.length * self.width

    def afficher_infos(self):
        print(f"\nLa longueur du rectangle est de {self.length}\nla largeur est de {self.width}\net l'aire est de {self.aire}\n")


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        self.aire = pi * self.rayon ** 2
        print(f"l'aire du cercle est de {self.aire}")

    def calcul_circonference(self):
        self.circonference = 2 * pi * self.rayon
        print(f"la circonférence du cercle est de {self.circonference}")


class Hero:
    def __init__(self, pv, force_atk, force_def, nom_hero):
        self.pv = random.randint(2, 20)
        self.force_atk = random.randint(1, 6)
        self.force_def = random.randint(1, 6)
        self.nom_hero = nom_hero

    def faire_attaque(self):
        self.attaque = self.force_atk + random.randint(1, 6)

    def recevoir_dommages(self, qte_dommage):
        self.pv -= qte_dommage - self.force_def

    #dire si le joueur est en vie en une ligne                                      <----Tu est rendu ici
    def est_vivant(self):




ligne = StringFoo()
ligne.set_string("hello!")
ligne.print_string()

r = Rectangle(2, 3)
r.calcul_aire()
r.afficher_infos()

c = Cercle(6)
c.calcul_aire()
c.calcul_circonference()
