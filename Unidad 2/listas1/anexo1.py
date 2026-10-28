from datos import pokemons


def main():

    # 1
    #pokemonMasPesado = max(pokemons, key=lambda p: p["peso_kg"])
    pokemonMasPesado = pokemons[0]
    for pokemon in pokemons:
        if pokemon["peso_kg"] > pokemonMasPesado["peso_kg"]:
            pokemonMasPesado = pokemon

    print(pokemonMasPesado["nombre"], pokemonMasPesado["peso_kg"])
    print()

    # 2
    mediaAltura = round(sum(p["altura_m"] for p in pokemons) / len(pokemons), 2)

    print("La media es ", mediaAltura, " metros.")
    print()

    # 3
    pBajoMedia = [(p["nombre"], p["altura_m"]) for p in pokemons if p["altura_m"] < mediaAltura]
    print(pBajoMedia)
    print()

    # 4
    for pokemon in pokemons:
        if "Agua" in pokemon["tipos"]:
            print(pokemon["nombre"], pokemon["tipos"])

    print()

    # 5
    for p in pokemons:
        print([p for t in p["tipos"] if t.endswith("a")])

    print()

    # 6
    pokemons.append(
        {
            "nombre": "Lapras",
            "generacion": 1,
            "categoria": "Transporte",
            "tipos": ["Agua", "Hielo"],
            "peso_kg": 220.0,
            "altura_m": 2.5,
        }
    )
    print(f"Se ha añadido el pokemon: {pokemons[-1]["nombre"]}")
    print()

    # 7
    """
    for i in range(len(pokemons) - 1, -1, -1):
        for tipo in pokemons[i]["tipos"]:
            if tipo == "Normal":
                print("Eliminando el pokemon: " + pokemons[i]["nombre"])
                del pokemons[i]
                break
    """
    for pokemon in pokemons[:]:
        if "Normal" in pokemon["tipos"]:
            pokemons.remove(pokemon)


if __name__ == "__main__":
    main()
