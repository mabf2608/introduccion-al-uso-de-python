def main():

    n = int(input("Introduce un número entero positivo mayor que 0: "))
    if (n <= 0):
        print("Error: Introduce un número válido.")
        return
    aux = n
    lista = [aux]

    while aux != 1:
        if(aux % 2 == 0):
            aux = aux // 2
        else:
            aux = aux * 3 + 1
        lista.append(aux)

    print(lista)

if __name__ == "__main__":
    main()