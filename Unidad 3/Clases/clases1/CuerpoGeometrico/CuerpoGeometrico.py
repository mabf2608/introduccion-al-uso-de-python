import math
from abc import ABC, abstractmethod


class CuerpoGeometrico(ABC):
    @abstractmethod
    def superficie(self):
        """Método abstracto que las subclases deben implementar."""

    @abstractmethod
    def volumen(self):
        """Método abstracto que las subclases deben implementar."""


class Cubo(CuerpoGeometrico):
    def __init__(self, lado: int = 1):
        self.lado = lado

    def superficie(self) -> int:
        superficieCara = self.lado**2
        return superficieCara * 6

    def volumen(self) -> int:
        return self.lado**3

    def __str__(self):
        return f"Cubo(Lado = {self.lado})"


class Cilindro(CuerpoGeometrico):
    def __init__(self, radio: int = 1, altura: int = 1):
        self.radio = radio
        self.altura = altura

    def superficie(self) -> float:
        return (math.pi * 2 * self.radio * (self.radio + self.altura))

    def volumen(self) -> float:
        return (math.pi * (self.radio**2) * self.altura)

    def __str__(self):
        return f"Cilindro(Radio = {self.radio}, Altura = {self.altura})"

"""
1. Crea un cilindro de radio 2 y altura 4.
2. Crea un cubo de lado 3.
3. Muestra la superficie y el volumen del cubo.
4. Muestra la superficie y el volumen del cilindro.
"""

cilindro1 = Cilindro(2, 4)
cubo1 = Cubo(3)

print(f"CUBO | Superficie = {cubo1.superficie()} | Volumen = {cubo1.volumen()}")
print(f"CILINDRO | Superficie = {cilindro1.superficie()} | Volumen = {cilindro1.volumen()}")