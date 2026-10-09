from datos import pokemons


def main():

    # 1
    pokemonMasPesado = pokemons[0]

    for pokemon in pokemons:
        if pokemon["peso_kg"] > pokemonMasPesado["peso_kg"]:
            pokemonMasPesado = pokemon

    print(pokemonMasPesado["nombre"], pokemonMasPesado["peso_kg"])
    print()

    # 2
    mediaAltura = 0

    for pokemon in pokemons:
        mediaAltura += pokemon["altura_m"]

    mediaAltura = mediaAltura / len(pokemons)
    print("La media es ", round(mediaAltura, 2), " metros.")
    print()

    # 3
    for pokemon in pokemons:
        if pokemon["altura_m"] < mediaAltura:
            print(pokemon["nombre"], pokemon["altura_m"])
    print()

    # 4
    for pokemon in pokemons:
        for tipo in pokemon["tipos"]:
            if tipo == "Agua":
                print(pokemon["nombre"], pokemon["tipos"])
                break
    print()

    # 5
    for pokemon in pokemons:
        for tipo in pokemon["tipos"]:
            if tipo[-1] == "a":
                print(pokemon)
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
    print("Se ha añadido el pokemon: " + pokemons[-1]["nombre"])
    print()

    # 7
    for i in range(len(pokemons) - 1, -1, -1):
        for tipo in pokemons[i]["tipos"]:
            if tipo == "Normal":
                print("Eliminando el pokemon: " + pokemons[i]["nombre"])
                del pokemons[i]
                break


if __name__ == "__main__":
    main()
