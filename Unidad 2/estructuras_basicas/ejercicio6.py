def main():
    
    password = input("Introduce una contraseña de 5 dígitos: ")

    while (password != "12345"):
        print("Error: Contraseña incorrecta.\n")
        password = input("Vuelve a introducir una contraseña de 5 dígitos: ")
    print("Contraseña correcta.\nBienvenido nuevamente.")

if __name__ == "__main__":
    main()