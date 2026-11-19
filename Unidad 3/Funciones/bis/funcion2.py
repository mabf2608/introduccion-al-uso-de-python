# Actividad 3.1.2 bis Ampliación - Miguel Ángel Bonilla Fernández

# Ejercicio 2 - Dada la lista de animales dispuesta más abajo, crea una función comprobar_estado, que reciba el nombre de una especie y devuelva los siguientes valores después de comprobar en la lista animales el número de ejemplares que tiene:

animales = [
    ["Lobo ibérico", "Mamífero", 2500],
    ["Lince ibérico", "Mamífero", 1668],
    ["Quebrantahuesos", "Ave", 2000],
    ["Oso pardo", "Mamífero", 500]
]

def comprobar_estado(nombre_especie: str) -> str:
    """
        Nos permite devolver el estado de la especie introducida como parámetro.

        Params:
            nombre_especie (str): Nombre de la especie a buscar en la lista.

        Returns:
            (str): Dependiendo de la especie introducida y de sus ejemplares devuelve un estado u otro.
    """

    especie = [especie for especie in animales if especie[0].upper() == nombre_especie.upper()]
    if not especie:
        raise ValueError("Introduce una especie que se encuentre en la lista.")

    ejemplares = especie[0][2]

    if ejemplares == 0:
        return "Extinto."
    elif ejemplares > 0 and ejemplares <= 500:
        return "En peligro crítico."
    elif ejemplares > 500 and ejemplares <= 2000:
        return "En peligro."
    elif ejemplares > 2000:
        return "Amenazado"
    else:
        raise ValueError("Introduce una especie que se encuentre en la lista.")
