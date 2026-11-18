# Actividad 3.1 - Miguel Ángel Bonilla Fernández

import math

# Ejercicio 1 - Crea una función llamada comprobarLetraDNI


def comprobarLetraDNI(cadena: str) -> bool:
    """
        Indica si un DNI es válido o no.
    
        Params:
            cadena (str): Cadena de texto con el DNI que queremos comprobar.
    
        Returns:
            (bool): Devuelve true si es válido y false si no lo es.
    """
    valido = True

    if len(cadena) != 9:
        valido = False
    else:
        num = cadena[:8]
        letra = cadena[8].upper()

        if not num.isdigit() or not letra.isalpha():
            valido = False
        else:
            num = int(num)
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            resto = letras[num % 23]

            if letra != resto:
                valido = False

    return valido


# Ejercicio 2 - Crea una función llamada convertirTemperatura


def convertirTemperatura(num: float, str1: str, str2: str) -> float:
    """
    Convierte la temperatura de una unidad a otra.

    Params:
        num (float): Temperatura que queremos convertir a otra unidad
        str1 (str): Unidad en la que se encuentra la temperatura actual
        str2 (str): Unidad a la que queremos pasar la temperatura actual

    Returns:
        (float): La temperatura inicial convertida de la unidad inicial a la final
    """

    unidades_validas = ("C", "K", "F")

    str1 = str1.upper()
    str2 = str2.upper()
    
    if str1 not in unidades_validas or str2 not in unidades_validas:
        raise ValueError("Las unidades posibles solo pueden ser C, F o K.")

    if str1 == str2:
        raise ValueError("Las unidades no pueden ser iguales.")
    aux = 0.0

    if str1 == "C":
        if num < -273.15:
            raise ValueError("La temperatura inicial no puede ser inferior a -273.15 C")
        if str2 == "F":
            aux = num * (9 / 5) + 32
        elif str2 == "K":
            aux = num + 273.15
    elif str1 == "F":
        if num < -459.67:
            raise ValueError("La temperatura inicial no puede ser inferior a -459.67 F")
        if str2 == "C":
            aux = (num - 32) * (5 / 9)
        elif str2 == "K":
            aux = (num - 32) * (5 / 9) + 273.15
    elif str1 == "K":
        if num < 0:
            raise ValueError("La temperatura inicial no puede ser inferior a 0 K")
        if str2 == "C":
            aux = num - 273.15
        elif str2 == "F":
            aux = (num - 273.15) * (9 / 5) + 32

    return round(aux, 2)


# Ejercicio 3 - Crea una función llamada calcularValorBruto


def calcularValorBruto(precio: float, iva: str) -> float:
    """Calcula el valor bruto de un producto partiendo del valor neto y el tipo de IVA aplicable

    Params:
        precio (float): Valor neto del producto, en euros.
        iva (str): Tipo de IVA aplicable. Solo acepta los valores GENERAL, REDUCIDO Y SUPERREDUCIDO.

    Returns:
        (float) : Valor bruto del producto tras aplicar el IVA.
    """
    unidades_validas = ("GENERAL", "REDUCIDO", "SUPERREDUCIDO")
    porcentaje = 0

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    iva = iva.upper()

    if iva not in unidades_validas:
        raise ValueError("El tipo de IVA solo puede ser GENERAL, REDUCIDO o SUPERREDUCIDO")

    if iva == "GENERAL":
        porcentaje = 21
    elif iva == "REDUCIDO":
        porcentaje = 10
    elif iva == "SUPERREDUCIDO":
        porcentaje = 4

    bruto = ((porcentaje * precio) / 100) + precio

    return math.ceil(bruto * 100) / 100
