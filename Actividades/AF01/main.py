from cargar import cargar_animes, cargar_consultas
from consultas import (
    cantidad_animes_genero, generos_distintos, promedio_rating_genero
)
from collections import namedtuple, deque


CONSULTAS = {
    0: cantidad_animes_genero,
    1: promedio_rating_genero,
    2: generos_distintos,
}


def chequear_tipos(animes, consultas):
    # No modificar
    if not isinstance(animes, dict) or not isinstance(list(animes.values())[0], tuple):
        print("Los animes no fueron guardados en las estructuas de datos pedidas.")
        return False
    if (not isinstance(consultas, deque) or
        not isinstance(consultas[0], tuple) or
            not isinstance(consultas[0][1], list)):
        print("Las consultas no fueron guardadas en las estructuras de datos pedidas.")
        return False
    return True


def procesar_consultas(animes, consultas):
    # No modificar
    for consulta in consultas:
        for idx, argumento in enumerate(consulta[1]):
            if "/" in argumento:
                nuevos_animes = []
                for anime in argumento.split("/"):
                    nuevos_animes.append(animes[anime])
                consulta[1][idx] = nuevos_animes
            else:
                consulta[1][idx] = animes[argumento]
    return consultas


def ejecutar_consultas(animes, consultas):
    # No modificar
    for indice, consulta in enumerate(consultas):
        tipo = int(consulta[0])
        args = consulta[1]
        resultado = CONSULTAS[tipo](*args)
        if not resultado:
            print(f'Consulta {indice}: {CONSULTAS[tipo].__name__} no implementado.')
        else:
            print(f'Consulta {indice}: {CONSULTAS[tipo].__name__}')
            print(f'Argumentos: {args}')
            print(f'Resultado: {resultado}')
        print()


def main():
    # No modificar
    animes = cargar_animes('animes.csv')
    consultas = cargar_consultas('consultas.csv')

    if not animes:
        print("cargar_animes no implementado.")
    if not consultas:
        print("cargar_consultas no implementado.")

    if animes and consultas and chequear_tipos(animes, consultas):
        print("Datos cargados y con estructuras pedidas.")
        consultas = procesar_consultas(animes, consultas)
        ejecutar_consultas(animes, consultas)


if __name__ == "__main__":
    main()
