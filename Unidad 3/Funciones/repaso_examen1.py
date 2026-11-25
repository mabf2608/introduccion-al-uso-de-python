def convertirVelocidad(num: float, str1: str, str2: str) -> float:
    """
    Convierte la velocidad de una unidad a otra.

    Params:
        num (float): Velocidad que queremos convertir a otra unidad
        str1 (str): Unidad en la que se encuentra la velocidad actual
        str2 (str): Unidad a la que queremos pasar la velocidad actual

    Returns:
        (float): La velocidad inicial convertida de la unidad inicial a la final
    """

    unidades_validas = ("N", "KMH", "MS")

    str1 = str1.upper()
    str2 = str2.upper()
    
    if str1 not in unidades_validas or str2 not in unidades_validas:
        raise ValueError("Las unidades posibles solo pueden ser N, KMH o MS.")

    if str1 == str2:
        raise ValueError("Las unidades no pueden ser iguales.")
    aux = 0.0

    if num < 0:
        raise ValueError("La velocidad inicial no puede ser inferior a 0.")

    if str1 == "N":
        if str2 == "KMH":
            aux = num * 1.852
        elif str2 == "MS":
            aux = (num * 1.852) / 3.6
    elif str1 == "KMH":
        if str2 == "N":
            aux = num / 1.852
        elif str2 == "MS":
            aux = num / 3.6
    elif str1 == "MS":
        if str2 == "N":
            aux = (num * 3.6) / 1.852
        elif str2 == "KMH":
            aux = num * 3.6

    return round(aux, 2)