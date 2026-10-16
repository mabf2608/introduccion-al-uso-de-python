from datos import personajes


def ejercicio1():
    personajes.append(
        {
            "nombre": "Son Gohan",
            "raza": "Saiyan",
            "nivel_pelea": 160000000,
            "tecnicas": ["KameHameHa", "Final Flash", "Genki Dama"],
            "atributos": {"fuerza": 86, "defensa": 87, "velocidad": 95}
        }
    )

def ejercicio2():
    for p in personajes:
        suma = p["atributos"]["fuerza"] + p["atributos"]["defensa"] + p["atributos"]["velocidad"]
        if (suma / 3) > 80:
            print(p)

def ejercicio3():
    suma = 0
    for p in personajes:
        suma += p["atributos"]["velocidad"]

    media = suma/len(personajes)
    for p in personajes:
        if p["atributos"]["velocidad"] > media:
            print(p)

def ejercicio4():
    for p in personajes:
        for t in p["tecnicas"]:
            if t == "Big Bang Attack":
                suma = p["atributos"]["fuerza"] + 10
                if suma > 100:
                    p["atributos"]["fuerza"] = 100
                else:
                    p["atributos"]["fuerza"] = suma

    for p in personajes:
        print(f"{p["nombre"]} {p["atributos"]["fuerza"]}")

def ejercicio5():
    fuerzaVegeta = 0
    for p in personajes:
        if p["nombre"] == "Vegeta":
            fuerzaVegeta = p["atributos"]["fuerza"]
            break

    for p in personajes:
        if p["nombre"] != "Vegeta" and fuerzaVegeta > p["atributos"]["defensa"]:
            print(f"{p["nombre"]} {p["atributos"]["defensa"]}")

def ejercicio6(): 
    for p in personajes[:]:
        if p["raza"] == "Saiyan":
                personajes.remove(p)

    for p in personajes:
        print(p)