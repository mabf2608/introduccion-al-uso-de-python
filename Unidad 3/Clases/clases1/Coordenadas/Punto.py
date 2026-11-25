import math


class Punto:
    def __init__(self, coordenadaX=0, coordenadaY=0):
        if (
            coordenadaX < -100
            or coordenadaX > 100
            or coordenadaY < -100
            or coordenadaY > 100
        ):
            raise ValueError("Las coordenadas deben estar enter -100 y 100")
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

    def __eq__(self, punto: "Punto"):
        return (
            self.coordenadaX == punto.coordenadaX
            and self.coordenadaY == punto.coordenadaY
        )

    def __str__(self):
        return f"Punto({self.coordenadaX}, {self.coordenadaY})"


class Segmento:
    def __init__ (self, puntoA: Punto = Punto(0, 0), puntoB: Punto = Punto(1, 1)):  # noqa: B008
        self.puntoA = puntoA
        self.puntoB = puntoB

    def longitud (self):
        return math.sqrt(
            (self.puntoB.coordenadaX - self.puntoA.coordenadaX) ** 2
            + (self.puntoB.coordenadaY - self.puntoA.coordenadaY) ** 2
        )

    def __eq__ (self, segmento: "Segmento"):
        return self.puntoA == segmento.puntoA and self.puntoB == segmento.puntoB

    def __str__ (self):
        return f"Segmento[{self.puntoA}, {self.puntoB}]"

"""
1. Crea los puntos (3,4) y (3,-3).
2. Crea un segmento que una ambos puntos.
3. Calcula la longitud del segmento.
"""

puntoA = Punto(3, 4)
puntoB = Punto(3, -3)

segmento = Segmento(puntoA, puntoB)

print(segmento.longitud())