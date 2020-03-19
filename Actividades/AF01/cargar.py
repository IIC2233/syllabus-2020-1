from collections import namedtuple, deque


def cargar_animes(path):
    # Abrimos el archivo de animes
    with open(path, 'r', encoding="utf-8") as file:
        # Leemos las lineas
        for line in file.readlines():
            # Las separamos por coma
            anime = line.strip().split(",")
            # Separamos los generos por slash
            anime[3] = anime[3].split("/")

    return


def cargar_consultas(path):
    # Abrimos el archivo de animes
    with open(path, 'r', encoding="utf-8") as file:
        # Leemos las lineas
        for line in file.readlines():
            # Los separamos por coma
            consulta = line.strip().split(";")

    return
