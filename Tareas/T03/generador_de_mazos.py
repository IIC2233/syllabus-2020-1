from random import choices

# -------------------------------------------------------------------------------------------------
#                                       PARÁMETROS
# -------------------------------------------------------------------------------------------------

# Indica el rango de los números
NUMEROS = (0, 5)
# Indica los distintos colores que puede tomar el mazo
COLORES = ('rojo', 'amarillo', 'verde', 'azul')

# Indica la cantidad de cartas de cada tipo
CANTIDAD_NORMAL = 1
CANTIDAD_MAS_2 = 2
CANTIDAD_SENTIDO = 2
CANTIDAD_COLOR = 2

# -------------------------------------------------------------------------------------------------
#                                       FUNCIÓN
# -------------------------------------------------------------------------------------------------


def sacar_cartas(cantidad_cartas):
    '''
    Función que genera un mazo y selecciona al azar la cantidad de cartas
    indicadas en el input.

    input: cantidad_cartas -> int
    output: lista de tuplas con las cartas -> list(tuple)
    '''
    mazo = []

    for color in COLORES:
        for numero in range(*NUMEROS):
            mazo += [(str(numero), color)] * CANTIDAD_NORMAL

        mazo += [('+2', color)] * CANTIDAD_MAS_2
        mazo += [('sentido', color)] * CANTIDAD_SENTIDO

    # TODO: ver si se pasa  la tupla con color vacio o sin color
    mazo += [('color', '')] * CANTIDAD_COLOR

    return choices(mazo, k=cantidad_cartas)


if __name__ == "__main__":
    for i in (0, 1, 5, 20, 100):
        cartas = sacar_cartas(i)
        print(len(cartas), cartas, '\n')
