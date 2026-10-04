def main():
    
    age = int(input("Introduce tu edad: "))

    if age < 0 and age < 18:
        print("Eres menor de edad.")
    elif age >= 18 and age < 120:
        print("Eres mayor de edad.")
    elif age >= 120:
        print("Eres un vampiro.")
    else:
        print("Error: la edad mínima es 0.")

if __name__ == "__main__":
    main()