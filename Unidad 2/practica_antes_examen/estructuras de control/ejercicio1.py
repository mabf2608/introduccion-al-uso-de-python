def main():

    latencia = int(input("Introduce la latencia:"))

    if latencia >= 0 and latencia <= 50:
        print("Conexión excelente.")
    elif latencia > 50 and latencia <= 120:
        print("Conexión aceptable.")
    elif latencia > 120:
        print("Lag severo.")
    else:
        print("Error: valor no válido.")

    match latencia:
        case x if x >= 0 and x <= 50:
            print("Conexión excelente.")
        case x if x > 50 and x <= 120:
            print("Conexión aceptable.")
        case x if x > 120:
            print("Lag severo.")
        case _:
            print("Error: valor no válido.")


if __name__ == "__main__":
    main()
