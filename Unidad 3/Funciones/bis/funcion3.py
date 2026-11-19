# Actividad 3.1.3 bis Ampliación - Miguel Ángel Bonilla Fernández

# Ejercicio 3 - Vamos a crear una función que permita convertir entre diferentes tipos de divisas. Crea una función llamada cambiar_divisa que reciba como parámetros una cantidad de dinero (que puede tener decimales), un string que represente la divisa en la que está, y otro string que represente la divisa en la que queramos convertir el dinero. La función devolverá el equivalente en la segunda divisa del dinero especificado en la primera divisa. Así, la función cambiar_divisa(10, “euro”, “dolar”) devolverá 10’90 dólares. Las divisas se escribirán sin tilde y será indiferente que estén en mayúsculas o minúsculas. La función permitirá cambiar entre euros, dólares y yenes, y devolverá el resultado con 3 decimales.

def cambiar_divisa(dinero_inicial: float, divisa: str, divisa_cambio: str) -> float:
    """
        Nos permite pasar de una divisa a otra la cantidad de dinero que le pasemos.
    
        Params:
            dinero_inicial (float): Dinero inicial que se pasa para cambiar de divisa.
            divisa (str): Divisa en la que está el dinero inicialmente.
            divisa_cambio (str): Divisa a la que se quiere cambiar.
    
        Returns:
            (float): Devuelve el valor del dinero inicial cambiado a la divisa indicada.
    """

    divisas_validas = ("EURO", "DOLAR", "YEN")
    dinero_final = 0.0

    if divisa.upper() not in divisas_validas or divisa_cambio.upper() not in divisas_validas:
        raise ValueError("Introduce divisas válidas sin tildes y en singular (dolar, yen, euro).")

    if dinero_inicial < 0:
        raise ValueError("Introduce una cantidad de dinero mayor que 0.0.")

    if divisa.upper() == "EURO":
        if divisa_cambio.upper() == "DOLAR":
            dinero_final = dinero_inicial * 1.09
        elif divisa_cambio.upper() == "YEN":
            dinero_final = dinero_inicial * 163.38
        else:
            raise ValueError("Introduce dos divisas diferentes.")
    elif divisa.upper() == "DOLAR":
        if divisa_cambio.upper() == "EURO":
            dinero_final = dinero_inicial * 0.92
        elif divisa_cambio.upper() == "YEN":
            dinero_final = dinero_inicial * 149.67
        else:
            raise ValueError("Introduce dos divisas diferentes.")
    elif divisa.upper() == "YEN":
        if divisa_cambio.upper() == "EURO":
            dinero_final = dinero_inicial * 0.0061
        elif divisa_cambio.upper() == "DOLAR":
            dinero_final = dinero_inicial * 0.0067
        else:
            raise ValueError("Introduce dos divisas diferentes.")
    else:
        raise ValueError("Valor no válido en divisa.")

    return round(dinero_final, 3)