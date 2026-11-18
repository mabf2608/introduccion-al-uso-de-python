class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        if saldo < 0:
            raise ValueError("El saldo debe ser igual o superior a cero.")
        self.titular = titular
        self.saldo = saldo

    def depositar (self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser igual o superior a cero.")
        self.saldo += cantidad

    def retirar (self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser igual o superior a cero.")
        elif cantidad > self.saldo:
            raise ValueError("La cantidad no puede ser superior al saldo.")
        self.saldo -= cantidad

    def __str__ (self):
        return f"Cuenta de {self.titular} | Saldo = {self.saldo}"