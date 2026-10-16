def main():

    base = float(input("Introduce la cuota base mensual: "))
    tipo = input("Introduce el tipo de tarifa (Mensual, Trimestral, Anual): ")

    if tipo == "Mensual":
        descuento = 0
    elif tipo == "Trimestral":
        descuento = (base * 10) / 100
    elif tipo == "Anual":
        descuento = (base * 25) / 100
    else:
        print("Error: Introduce un valor válido.")

    match tipo:
        case "Mensual":
            descuento = 0
        case "Trimestral":
            descuento = (base * 10) / 100
        case "Anual":
            descuento = (base * 25) / 100
        case _:
            print("Error: Introduce un valor válido.")

    print(f"El precio final es: {base - descuento}€ mensuales.")


if __name__ == "__main__":
    main()
