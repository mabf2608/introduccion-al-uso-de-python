def main():
    
    x = int(input("Introduce el primer número entero: "))
    y = int(input("Introduce el segundo número entero: "))
    aux = x

    if x > y:
        print("Error: el primer número tiene que ser menor que el segundo.")
        return

    for i in range (x, y):
        if i % 2 == 0:
            print(str(i))

    while aux < y:
        if aux % 2 == 0:
            print(str(aux))
        aux += 1

if __name__ == "__main__":
    main()