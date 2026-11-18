class Jarra:
    def __init__(self, capacidad, contenido=0):
        if capacidad <= 0:
            raise ValueError("La capacidad tiene que ser superior a 0.")

        if contenido < 0:
            raise ValueError("El contenido tiene que ser superior o igual a 0.")

        self.capacidad = capacidad
        self.contenido = min(contenido, capacidad)

    def llenar(self):
        self.contenido = self.capacidad

    def vaciar(self):
        self.contenido = 0

    def servir(self, cantidadAServir):
        if cantidadAServir > self.contenido or cantidadAServir < 0:
            raise ValueError(
                "La cantidad a servir no puede ser mayor que el contenido de la jarra ni menor que 0."
            )
        self.contenido -= cantidadAServir

    def llenar_desde(self, jarra: "Jarra"):
        if (self.capacidad - self.contenido) >= jarra.contenido:
            self.contenido += jarra.contenido
            jarra.vaciar()
        else:
            jarra.contenido -= self.capacidad - self.contenido
            self.llenar()

    def __str__(self):
        return f"La Jarra tiene {self.capacidad} L de capacidad y contiene {self.contenido} L."
