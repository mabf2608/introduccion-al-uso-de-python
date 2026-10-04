def main():
    
    notaNumerica = int(input("Introduce una nota numérica: "))

    """
    if notaNumerica >= 0 and notaNumerica < 5:
        print("Suspenso")
    elif notaNumerica == 5:
        print("Suficiente")
    elif notaNumerica == 6:
        print("Bien")
    elif notaNumerica > 6 and notaNumerica < 9:
        print("Notable")
    elif notaNumerica > 8 and notaNumerica < 11:
        print("Sobresaliente")
    else:
        print("Nota no válida")
    """

    match notaNumerica:
        case 0 | 1 | 2 | 3 | 4: 
            print("Suspenso")
        case 5:
            print("Suficiente")
        case 6:
            print("Bien")
        case 7 | 8:
            print("Notable")
        case 9 | 10:
            print("Sobresaliente")
        case _:
            print("No válida")
            
if __name__ == "__main__":
    main()