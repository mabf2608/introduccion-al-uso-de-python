def main():

    numero1 = int(input("Introduce el primer número entero: "))
    numero2 = int(input("Introduce el segundo número entero: "))

    if numero2 < numero1:
        print("Error: el segundo valor tiene que ser mayor que el primero.")
        return

    for i in range(numero1, numero2 + 1):
        if i % 3 == 0:
            print(i)

    i = numero1
    while i < numero2 + 1:
        if i % 3 == 0:
            print(i)
        i += 1

if __name__ == "__main__":
    main()
