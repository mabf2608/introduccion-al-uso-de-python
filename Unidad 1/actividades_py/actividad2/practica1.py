def main():
    #Listas
    lista1 = ["Manzana", "Pera", "Melocotón"]
    lista2 = ["Kiwi", "Sandía", "Melón"]
    lista1.extend(lista2)
    print(lista1[-1])
    #Tupla
    tupla = (3, 5, 7)
    print(tupla[0])
    #Rango
    inicio = int(input("Introduce el inicio del rango que deseas crear: "))
    fin = int(input("Introduce el final del rango que deseas crear: "))
    salto = int(input("Introduce el salto del rango que deseas crear: "))
    rango = range(inicio, fin, salto)
    print(rango)
if __name__ == "__main__":
    main()