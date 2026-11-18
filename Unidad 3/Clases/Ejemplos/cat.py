class Cat:

    def __init__(self, raza, nombre, peso):
        self.raza = raza
        self.nombre = nombre
        self.peso = peso

    def maullar(self):
        print(f"{self.nombre} está maullando.")

    def toString(self):
        print(f"{self.nombre} es de la raza {self.raza} y pesa {self.peso}")