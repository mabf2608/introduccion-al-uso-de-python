def main():

    base = int(input("Introduce la base: "))
    potencia = int(input("Introduce la potencia: "))

    if base < 1:
        print("Error: Introduce una base mayor o igual que 1.")
        return

    if potencia < 0:
        print("Error: Introduce una potencia mayor o igual que 0.")
        return

    x = base ** potencia

    print(f"El resultado de elevar {base} a {potencia} es {x}.")

if __name__ == "__main__":
    main()