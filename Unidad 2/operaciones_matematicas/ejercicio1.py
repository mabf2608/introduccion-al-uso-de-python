def main():

    x = int(input("Introduce un número entero: "))
    aux = 0

    if x < 1:
        print("Error: Introduce un número mayor o igual que 1.")
        return

    for i in range(1, x + 1):
        aux += i

    print(f"El sumatorio es {aux}.")

if __name__ == "__main__":
    main()