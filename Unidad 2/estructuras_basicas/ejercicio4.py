def main():
    
    rain = int(input("Introduce los mm de lluvia: "))

    """
    if rain >= 0 and rain < 60:
        print("No hay alerta.")
    elif rain >= 60 and rain < 120:
        print("Alerta Amarilla.")
    elif rain >= 120:
        print("Alerta Roja.")
    else:
        print("Error: Indica unos mm de lluvia correctos.")
        return
    """
    
    match rain:
        case x if x >= 0 and x < 60:
            print("No hay alerta.")
        case x if x >= 60 and x < 120:
            print("Alerta Amarilla.")
        case x if x >= 120:
            print("Alerta Roja.")
        case _:
            print("Error: Indica unos mm de lluvia correctos.")

if __name__ == "__main__":
    main()