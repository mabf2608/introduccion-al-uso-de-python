def main():

    filas = int(input("Introduce un número de filas: "))

    if filas < 1:
        print("Error: Introduce un número válido.")
        return

    for i in range(1, filas + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

if __name__ == "__main__":
    main()