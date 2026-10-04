def main():

    number = int(input("Introduce un número para saber si es primo: "))

    if number <= 1:
        print("No es primo")
        return

    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            print(f"{number} no es primo.")
            return

    print(f"{number} es primo.")

if __name__ == "__main__":
    main()