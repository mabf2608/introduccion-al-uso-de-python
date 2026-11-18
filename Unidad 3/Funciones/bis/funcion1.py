# Actividad 3.1.1 bis Ampliación - Miguel Ángel Bonilla Fernández

# Ejercicio 1 - Crea una función llamada aplicar_funcion que nos permita ejecutar el cálculo de varios algoritmos matemáticos.

def sumatorio(n: int) -> int:
    if n < 0:
        raise ValueError("Introduce un número positivo entero o 0.")
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def factorial(n: int) -> int:
    if n < 1:
        raise ValueError("Introduce un número positivo entero.")
    mult = 1
    for i in range(1, n + 1):
        mult *= i
    return mult

def aplicar_funcion(n: int, calculo: str) -> int:
    """
    Nos permite usar uno de los algoritmos dados con un número entero positivo.

    Params:
        n (int): Numero que se va a usar en los algoritmos
        calculo (str): Algoritmo seleccionado

    Returns:
        (int): Muestra por pantalla y devuelve el valor final del algoritmo usado en n.
    """
    calculos_validos = ("FACTORIAL", "SUMATORIO")
    valor_final = 0

    calculo = calculo.upper()
    if calculo not in calculos_validos:
        raise ValueError("Solo se permiten los cálculos factorial y sumatorio.")

    if calculo == "FACTORIAL":
        valor_final = factorial(n)
    elif calculo == "SUMATORIO":
        valor_final = sumatorio(n)

    print(f"El {calculo} de {n} es {valor_final}.")
    return valor_final