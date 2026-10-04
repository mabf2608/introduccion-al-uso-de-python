def main():
    
    price = float(input("Introduce el valor del producto: "))
    iva = input("Introduce el tipo de IVA: ").strip().capitalize()

    """
    if iva == "General":
        iva = 21
    elif iva == "Reducido":
        iva = 10
    elif iva == "Superreducido":
        iva = 4
    else:
        print("Error: Tipo de IVA no válido, saliendo del programa.")
        return
    """

    match iva:
        case "General":
            iva = 21
        case "Reducido":
            iva = 10
        case "Superreducido":
            iva = 4
        case _:
            print("Error: Tipo de IVA no válido, saliendo del programa.")
            return
        
    price = ((iva * price) / 100) + price
    print(str(price))
    
if __name__ == "__main__":
    main()