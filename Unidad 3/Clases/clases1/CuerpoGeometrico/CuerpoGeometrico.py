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

    def __str__(self):
        return f"Cilindro(Radio = {self.radio}, Altura = {self.altura})"
