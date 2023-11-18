from abc import ABC, abstractmethod
from typing import List


"""
Old code:

class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
"""


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Turtle(Animal):
    def make_sound(self):
        return "turtle sound"


class Chicken(Animal):
    def make_sound(self):
        return "chicken sound"


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Turtle(), Chicken()]
animal_sound(animals)
