from datos import personajes_frieren


def main():

    # 1
    edadHumanos = sum(p["edad"] for p in personajes_frieren if p["raza"] == "Humano")
    total_humanos = sum(p["raza"] == "Humano" for p in personajes_frieren)

    mediaEdadHumanos = round(edadHumanos / total_humanos, 2) if total_humanos > 0 else 0

    print("La media de edad de la raza humana es: " + str(mediaEdadHumanos))
    print()

    # 2
    for p in personajes_frieren:
        if "Magos de Primera Clase" in p["afiliacion"]:
            print(p["nombre"], p["raza"])

    print()

    # 3
    for p in personajes_frieren:
        if "Grupo de los Cuatro Héroes" in p["afiliacion"]:
            print([p["nombre"], p["raza"], p["edad"]] for p in personajes_frieren if "Grupo de los Cuatro Héroes" in p["afiliacion"] )

    print()
    # 4
    personajes_frieren.append(
        {
            "nombre": "Kraft",
            "raza": "Elfo",
            "clase": "Guerrero",
            "edad": 3000,
            "afiliacion": ["Monjes Guerreros"],
        }
    )
    print("Se ha añadido al personaje: " + personajes_frieren[-1]["nombre"])
    print()

    # 5
    for p in personajes_frieren[:]:
        if p["raza"] == "Demonio":
            print(f"Eliminando al personaje: {p["nombre"]}")
            personajes_frieren.remove(p)
    print()

    # 6
    for p in personajes_frieren[:]:
        if p["raza"] == "Elfo":
            print(f"Añadiendo al personaje {p["nombre"]} a la afiliciacion Elfos Supervivientes del Examen de Python")
            p["afiliacion"].append("Elfos Supervivientes del Examen de Python" )
    print()

    # 7
    for p in personajes_frieren:
        if "Asociación Continental de Magia" in p["afiliacion"]:
            print(f"Eliminando afiliación de: {p['nombre']}.")
            p["afiliacion"].remove("Asociación Continental de Magia")
    print()

    # 8
    for p in personajes_frieren:
        if p["raza"] == "Humano" and p["edad"] >= 100:
            p["raza"] = "Zombie"
            print(f"El personaje {p['nombre']}, ha dejado de ser Humano y ahora es un Zombie.")


if __name__ == "__main__":
    main()
