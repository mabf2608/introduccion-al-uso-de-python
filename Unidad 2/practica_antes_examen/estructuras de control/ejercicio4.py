def main():

    i = 0
    codigo = 9876

    while (i < 3):
        intento = int(input("Introduce la contraseña: "))
        if(intento == codigo):
            print("Acceso concedido.")
            break
        else:
            if i < 3:
                print("Error, vuelva a introducir la contraseña")
            i += 1

    if (i == 3):
                print("Tarjeta bloqueada.")
                
if __name__ == "__main__":
    main()