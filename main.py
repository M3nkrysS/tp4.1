"""
Lucas B.T.
Gr: 401
introduction à POOP
"""
import random
from math import pi
from dataclasses import dataclass


def de_vinght():
    nbr = random.randint(1, 20)
    return nbr


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
        print(f"la circonférence du cercle est de {self.circonference}\n")


class Hero:
    def __init__(self, nom_hero, pv, force_atk, force_def, vivant):
        self.nom_hero = nom_hero
        self.pv = pv
        self.force_atk = force_atk
        self.force_def = force_def
        self.vivant = vivant

    def faire_attaque(self):
        self.attaque = self.force_atk + random.randint(1, 6)

    def recevoir_dommages(self, qte_dommage):
        self.pv -= qte_dommage - self.force_def

    def est_vivant(self, vivant):
        self.vivant = vivant
        self.vivant = True
        if self.pv <= 0:
            self.vivant = False
        else:
            pass

    def vie(self):
        print(self.vivant)


@dataclass
class PersonnageDnD:
    force: int = de_vinght()
    dexterite: int = de_vinght()
    constitution: int = de_vinght()
    intelligence: int = de_vinght()
    sagesse: int = de_vinght()
    charisme: int = de_vinght()


ligne = StringFoo()
ligne.set_string("hello!")
ligne.print_string()

r = Rectangle(2, 3)
r.calcul_aire()
r.afficher_infos()

c = Cercle(6)
c.calcul_aire()
c.calcul_circonference()

h = Hero("George", random.randint(2, 20), random.randint(1, 6), random.randint(1, 6), True)
h.vie()
p = PersonnageDnD
print(p.force)
