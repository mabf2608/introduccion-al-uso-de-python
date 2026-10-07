def main():

    x = int(input("Introduce un número entero: "))
    i = 0

    if x < 0:
        print("Error: Introduce un número mayor o igual que 0.")
        return

    numbers = []
    a, b = 0, 1

    while i < x:
        numbers.append(a)
        a, b = b, a + b
        i+=1

    print(numbers)

if __name__ == "__main__":
    main()