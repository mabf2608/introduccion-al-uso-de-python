def main():

    x = int(input("Introduce el primer número del rango: "))
    y = int(input("Introduce el segundo número del rango: "))

    if(x > y):
        print("Error: Introduce valores válidos, el primero tiene que ser menor.")
        return
    
    for i in range(x, y):
        if i < 2:
            print("Este número no es primo.")
        else:
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    print(f"{i} no es primo.")
                    break
            else:
                print(f"{i} es primo.")

if __name__ == "__main__":
    main()