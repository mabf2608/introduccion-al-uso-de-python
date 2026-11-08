# Actividad 3.1 - Miguel Ángel Bonilla Fernández

import math

# Ejercicio 1 - Crea una función llamada comprobarLetraDNI


def comprobarLetraDNI(cadena: str) -> bool:
    if len(cadena) != 9:
        return False

    num = cadena[:8]
    letra = cadena[8].upper()

    if not num.isdigit():
        return False
    if not letra.isalpha():
        return False

    num = int(num)
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resto = letras[num % 23]

    return letra == resto


# Ejercicio 2 - Crea una función llamada convertirTemperatura


def convertirTemperatura(num: float, str1: str, str2: str) -> float:
    unidades_validas = ("C", "K", "F")
    if str1 not in unidades_validas or str2 not in unidades_validas:
        return 0.0

    if str1 == str2:
        return round(num, 2)

    aux = 0.0
    if str1 == "C":
        if str2 == "F":
            aux = num * (9 / 5) + 32
        elif str2 == "K":
            aux = num + 273.15
    if str1 == "F":
        if str2 == "C":
            aux = (num - 32) * (5 / 9)
        elif str2 == "K":
            aux = (num - 32) * (5 / 9) + 273.15
    if str1 == "K":
        if str2 == "C":
            aux = num - 273.15
        elif str2 == "F":
            aux = (num - 273.15) * (9 / 5) + 32

    return round(aux, 2)


# Ejercicio 3 - Crea una función llamada calcularValorBruto


def calcularValorBruto(precio: float, iva: str) -> float:
    unidades_validas = ("GENERAL", "REDUCIDO", "SUPERREDUCIDO")
    aux = 0.0
    porcentaje = 0
    if iva not in unidades_validas:
        return aux

    if iva == "GENERAL":
        porcentaje = 21
    elif iva == "REDUCIDO":
        porcentaje = 10
    elif iva == "SUPERREDUCIDO":
        porcentaje = 4

    bruto = ((porcentaje * precio) / 100) + precio

    return math.ceil(bruto * 100) / 100
