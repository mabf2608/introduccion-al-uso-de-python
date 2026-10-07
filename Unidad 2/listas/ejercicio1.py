def main():

    pokemons = [
        {
        "nombre": "Bulbasaur",
        "generacion": 1,

        "categoria": "Semilla",
        "tipos": ["Planta", "Veneno"],
        "peso_kg": 6.9,
        "altura_m": 0.7
        },
        {
        "nombre": "Charizard",
        "generacion": 1,
        "categoria": "Llama",
        "tipos": ["Fuego", "Volador"],
        "peso_kg": 90.5,
        "altura_m": 1.7
        },
        {
        "nombre": "Squirtle",
        "generacion": 1,
        "categoria": "Tortuguita",
        "tipos": ["Agua"],
        "peso_kg": 9.0,
        "altura_m": 0.5
        },
        {
        "nombre": "Pikachu",
        "generacion": 1,
        "categoria": "Ratón",
        "tipos": ["Eléctrico"],
        "peso_kg": 6.0,
        "altura_m": 0.4
        },
        {
        "nombre": "Jigglypuff",
        "generacion": 1,
        "categoria": "Globo",
        "tipos": ["Normal", "Hada"],
        "peso_kg": 5.5,
        "altura_m": 0.5
        },
        {
        "nombre": "Eevee",
        "generacion": 1,
        "categoria": "Evolución",
        "tipos": ["Normal"],
        "peso_kg": 6.5,
        "altura_m": 0.3
        },
        {
        "nombre": "Lucario",
        "generacion": 4,

        "categoria": "Aura",
        "tipos": ["Lucha", "Acero"],
        "peso_kg": 54.0,
        "altura_m": 1.2
        },
        {
        "nombre": "Gardevoir",
        "generacion": 3,
        "categoria": "Envolvente",
        "tipos": ["Psíquico", "Hada"],
        "peso_kg": 48.4,
        "altura_m": 1.6
        },
        {
        "nombre": "Greninja",
        "generacion": 6,
        "categoria": "Ninja",
        "tipos": ["Agua", "Siniestro"],
        "peso_kg": 40.0,
        "altura_m": 1.5
        }
    ]

    #1
    pokemonMasPesado = pokemons[0]

    for pokemon in pokemons:
        if pokemon["peso_kg"] > pokemonMasPesado["peso_kg"]:
            pokemonMasPesado = pokemon

    print(pokemonMasPesado)

    #2
    mediaAltura = 0

    for pokemon in pokemons:
        mediaAltura += pokemon["altura_m"]

    mediaAltura = mediaAltura / len(pokemons)
    print(mediaAltura)

    #3

if __name__ == "__main__":
    main()