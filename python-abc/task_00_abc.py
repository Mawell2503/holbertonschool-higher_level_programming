#!/usr/bin/python3
"""Importing a abstract class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Return animal sound"""
        pass

class Dog(Animal):
    """Dog subclass"""

    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat subclass"""

    def sound(self):
        return "Meow"