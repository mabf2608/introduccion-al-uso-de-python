# Miguel Ángel Bonilla Fernández 2ºDAM
from datos import personajes


def ejercicio1():
    print(
        [
            p["nombre"]
            for p in personajes
            if p["afiliacion"] == "Cuerpo de Exploración" and p["vivo"] == True
        ]
    )


def ejercicio2():
    print(
        [
            p["nombre"]
            for p in personajes
            if p["afiliacion"] == "Cuerpo de Exploración"
            and "Supervivencia" in p["habilidades"]
            and "Sigilo" in p["habilidades"]
        ]
    )


def ejercicio3():
    print(
        [
            (p["nombre"], p["afiliacion"])
            for p in personajes
            if p["afiliacion"] != "Cuerpo de Exploración"
        ]
    )


def ejercicio4():
    print(
        [
            f"{p['nombre']} ({p['afiliacion']})"
            for p in personajes
            if p["registro_combate"]["misiones_completadas"] >= 20
        ]
    )


def ejercicio5():
    print(
        [
            (p["nombre"], (int)(p["estatura_m"] * 100))
            for p in personajes
            if p["estatura_m"] > 1.70
        ]
    )


def ejercicio6():
    print([h for p in personajes for h in p["habilidades"]])


def ejercicio7():
    print(
        [
            p["nombre"]
            for p in personajes
            if (
                p["registro_combate"]["titanes_solo"]
                + p["registro_combate"]["titanes_equipo"]
            )
            >= 5
        ]
    )


def ejercicio8():
    print(
        [
            {
                "nombre": p["nombre"],
                "titanes_totales": p["registro_combate"]["titanes_solo"]
                + p["registro_combate"]["titanes_equipo"],
            }
            for p in personajes
        ]
    )


def ejercicio9():
    mediaAltura = round(sum(p["estatura_m"] for p in personajes) / len(personajes), 2)
    print(mediaAltura)


def ejercicio10():
    mediaAltura = round(sum(p["estatura_m"] for p in personajes) / len(personajes), 2)
    tupla = [
        (p["nombre"], p["estatura_m"])
        for p in personajes
        if p["estatura_m"] > mediaAltura
    ]
    print(tupla)