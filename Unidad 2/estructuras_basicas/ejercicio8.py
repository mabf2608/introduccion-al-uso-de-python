def main():

    videojuegos = [
    {"titulo": "The Legend of Zelda: BOTW", "consola": "Nintendo Switch", "precio": 59.99},
    {"titulo": "Hollow Knight", "consola": "PC", "precio": 14.99},
    {"titulo": "Stardew Valley", "consola": "PlayStation 4", "precio": 13.99},
    {"titulo": "Assassin's Creed Shadows", "consola": "PlayStation 5", "precio": 69.99},
    {"titulo": "Resident Evil: Requiem", "consola": "PlayStation 5", "precio": 79.99},
    {"titulo": "Trails in the Sky 1st Chapter", "consola": "Nintendo Switch", "precio": 49.9}
    ]

    for game in videojuegos:
        if game["precio"] > 20:
            print(game["titulo"])

if __name__ == "__main__":
    main()