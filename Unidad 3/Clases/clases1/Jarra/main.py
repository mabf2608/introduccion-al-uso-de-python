from Jarra import Jarra


def main():
    jarra1 = Jarra(500)
    jarra2 = Jarra(1000)
    print("1.-")
    print(f"{jarra1} \n{jarra2}")

    jarra1.llenar()
    jarra2.llenar()
    print("2.-")
    print(f"{jarra1} \n{jarra2}")

    jarra2.vaciar()
    print("3.-")
    print(jarra2)

    jarra1.servir(200)
    print("4.-")
    print(jarra1)

    jarra2.llenar_desde(jarra1)
    print("5.-")
    print(f"{jarra1} \n{jarra2}")

if __name__ == "__main__":
    main()