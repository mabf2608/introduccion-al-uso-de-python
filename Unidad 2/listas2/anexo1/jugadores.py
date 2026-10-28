from datos import jugadores


def ejercicio1():
    print([j["nombre"] for j in jugadores])


def ejercicio2():
    print([j for j in jugadores if j["dorsal"] == 10])


def ejercicio3():
    print([j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"])


def ejercicio4():
    print([j["nombre"] for j in jugadores if j["atributos"]["pase"] >= 9])


def ejercicio5():
    print([j for j in jugadores if "ruleta" in j["filigranas"]])


def ejercicio6():
    print(
        [
            j
            for j in jugadores
            if j["atributos"]["tiro"] >= 8 and j["atributos"]["regate"] >= 9
        ]
    )


def ejercicio7():
    print([f"{j['nombre']} ({j['equipo']})" for j in jugadores])


def ejercicio8():
    print(
        [
            (j["nombre"], "Goleador" if j["atributos"]["tiro"] >= 9 else "Asistente")
            for j in jugadores
        ]
    )


def ejercicio9():
    print([j["nombre"] for j in jugadores if len(j["filigranas"]) > 2])


def ejercicio10():
    #print([f for j in jugadores for f in j["filigranas"]])
    print(*[f for j in jugadores for f in j["filigranas"]])