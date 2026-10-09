from datos import personajes_frieren


def main():

    # 1
    mediaEdadHumanos = 0
    cantidadHumanos = 0.0
    for personaje in personajes_frieren:
        if personaje["raza"] == "Humano":
            mediaEdadHumanos += personaje["edad"]
        if personaje["raza"] == "Humano":
            cantidadHumanos += 1
    mediaEdadHumanos /= cantidadHumanos
    print("La media de edad de la raza humana es: " + str(mediaEdadHumanos))
    print()

    # 2
    for personaje in personajes_frieren:
        for afiliciacion in personaje["afiliacion"]:
            if afiliciacion == "Magos de Primera Clase":
                print(personaje["nombre"], personaje["raza"])
                break
    print()

    # 3
    for personaje in personajes_frieren:
        for afiliciacion in personaje["afiliacion"]:
            if afiliciacion == "Grupo de los Cuatro Héroes":
                print(personaje["nombre"], personaje["raza"], personaje["edad"])
                break

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
    for i in range(len(personajes_frieren) - 1, -1, -1):
        if personajes_frieren[i]["raza"] == "Demonio":
            print("Eliminando al personaje: " + personajes_frieren[i]["nombre"])
            del personajes_frieren[i]
    print()

    # 6
    for i in range(len(personajes_frieren) - 1, -1, -1):
        if personajes_frieren[i]["raza"] == "Elfo":
            print(
                "Añadiendo al personaje "
                + personajes_frieren[i]["nombre"]
                + " a la afiliciacion Elfos Supervivientes del Examen de Python"
            )
            personajes_frieren[i]["afiliacion"].append(
                "Elfos Supervivientes del Examen de Python"
            )
    print()

    # 7
    for personaje in personajes_frieren:
        for i in range(len(personaje["afiliacion"]) - 1, -1, -1):
            if personaje["afiliacion"][i] == "Asociación Continental de Magia":
                print(f"Eliminando afiliación de: {personaje['nombre']}.")
                del personaje["afiliacion"][i]
                break
    print()

    # 8
    for personaje in personajes_frieren:
        if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
            personaje["raza"] = "Zombie"
            print(
                f"El personaje {personaje['nombre']}, ha dejado de ser Humano y ahora es un Zombie."
            )


if __name__ == "__main__":
    main()
