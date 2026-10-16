from datos import agentes, comandos


def main():
    """Ejercicio 1"""
    for c in comandos:
        if c[0] == "g":
            print(c)

    """Ejercicio 2"""
    media_horas = 0
    for a in agentes:
        media_horas += a["horas_jugadas"]
    media_horas = media_horas / len(agentes)
    print(round(media_horas, 2))

    """Ejercicio 3"""
    for a in agentes:
        for h in a["habilidades"]:
            if h == "Humo":
                print(f"Nombre: {a['nombre']}| Origen: {a['origen']}")

    """Ejercicio 4"""
    for a in agentes:
        if a["horas_jugadas"] > 100 and a["afiliacion"] == "Protocolo Valorant":
            print(f"Nombre: {a["nombre"]} | Rol: {a["rol"]} | Horas: {a["horas_jugadas"]}")

    """Ejercicio 5"""
    agentes.append(
        {
            "nombre": "Brimstone",
            "origen": "EEUU",
            "rol": "Controlador",
            "horas_jugadas": 67,
            "afiliacion": "Protocolo Valorant",
            "habilidades": ["Humo", "Molo", "Rayo Láser"]
        }
    )
    print(agentes[-1])

    """Ejercicio 6"""
    for i in range(len(agentes) - 1, - 1, - 1):
        if agentes[i]["rol"] == "Centinela":
            print(f"Eliminando al personaje {agentes[i]["nombre"]}")
            del agentes[i]

    """Ejercicio 7"""
    for a in agentes:
        if a["origen"] == "España" or a["origen"] == "México":
            a["habilidades"].append("Habla Hispana")
            print(a["nombre"], a["habilidades"])

    """Ejercicio 8"""
    for a in agentes:
        for i in range(len(a["habilidades"])- 1, - 1, -1):
            if a["habilidades"][i] == "Flash":
                del a["habilidades"][i]
                print(a)

    """Ejercicio 9"""
    for a in agentes:
        if a["horas_jugadas"] >= 300:
            a["rol"] = "Veterano"
            print(a)
            
if __name__ == "__main__":
    main()
