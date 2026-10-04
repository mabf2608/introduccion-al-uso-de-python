def main():

    x = int(input("Introduce un número entero: "))

    if x < 0:
        print("Error: Introduce un número mayor o igual que 0.")
        return

    numbers = []
    a, b = 0, 1

    while a <= x:
        numbers.append(a)
        a, b = b, a + b

    print(numbers)

if __name__ == "__main__":
    main()