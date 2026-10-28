from datos import series


def ejercicio1():
    print([s["titulo"] for s in series if "Animación" in s["generos"]])


def ejercicio2():
    print(
        [
            s["titulo"]
            for s in series
            if "Fantasía" in s["generos"]
            or "Misterio" in s["generos"]
        ]
    )


def ejercicio3():
    print([s["titulo"] for s in series if s["nota"] >= 9 and len(s["generos"]) >= 3])


def ejercicio4():
    print(
        [
            (s["titulo"], r["nota"])
            for s in series
            for r in s["reseñas"]
            if r["usuario"] == "Elena"
        ]
    )

def ejercicio5():
    print(
        [
            r["comentario"]
            for s in series
            for r in s["reseñas"]
            if len(r["comentario"]) > 40
        ]
    )

def ejercicio6():
    print(
        [
            f"La serie {s["titulo"]} tiene {len(s["reseñas"])} reseñas."
            for s in series
        ]
    )

def ejercicio7():
    print(
        [
            (s["titulo"], r["comentario"])
            for s in series
            for r in s["reseñas"]
            if r["nota"] == 10
        ]
    )

def ejercicio8():
    print(
        [
            (
                s["titulo"], "Obra Maestra" 
                if sum(r["nota"] for r in s["reseñas"]) / len(s["reseñas"]) >= 9 
                else "Gran Serie"
            )
            for s in series
        ]
    )

def ejercicio9():
    print([g for s in series for g in s["generos"]])

def ejercicio10():
    print(
        [
            r["usuario"]
            for s in series
            for r in s["reseñas"]
            if "Drama" in s["generos"]
        ]
    )