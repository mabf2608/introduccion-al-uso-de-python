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
    print([p for p in personajes if (p["atributos"]["fuerza"] + p["atributos"]["defensa"] + p["atributos"]["velocidad"])/3 > 80])

def ejercicio3():
    media = sum(p["atributos"]["velocidad"] for p in personajes) / len(personajes)

    print ([p for p in personajes if p["atributos"]["velocidad"] > media])

def ejercicio4():
    for p in personajes:
        if "Big Bang Attack" in p["tecnicas"]:
            p["atributos"]["fuerza"] = min(p["atributos"]["fuerza"] + 10, 100)
        print(f"{p["nombre"]} {p["atributos"]["fuerza"]}")

def ejercicio5():
    fuerzaVegeta = [p["atributos"]["fuerza"] for p in personajes if p["nombre"] == "Vegeta"]

    for p in personajes:
        if p["nombre"] != "Vegeta" and fuerzaVegeta > p["atributos"]["defensa"]:
            print(f"{p["nombre"]} {p["atributos"]["defensa"]}")

def ejercicio6(): 
    for p in personajes[:]:
        if p["raza"] == "Saiyan":
                personajes.remove(p)

    for p in personajes:
        print(p)