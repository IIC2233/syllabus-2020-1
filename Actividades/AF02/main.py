from cargado import cargar_jugadores, imprimir_equipos
from combate import jugar, anunciar_ganadores

if __name__ == '__main__':

    # La siguiente función se encuentra en cargado.py y 
    # carga e instancia tanto a los ayudantes como a los alumnos(as) que van a competir.
    alumnos, ayudantes = cargar_jugadores()

    # La siguiente función imprime por equipo y por especialidad, respectivamente,
    # a los competidores ya cargados e instanciados.
    # Esto te servirá para ver si implementaste bien las clases pedidas.
    imprimir_equipos(alumnos, ayudantes)

    # Ahora se hace una tupla de los competidores según su equipo y del puntaje.
    equipo_alumnos = (alumnos, 0)
    equipo_ayudantes = (ayudantes, 0)

    print("¡Comienzan los juegos!")
    # La siguiente iteración sirve para que se juegue una partida de cada juego,
    # donde la función jugar retornará la misma tupla pero con el puntaje actualizado.
    for ronda in ['mesa', 'cartas', 'combate', 'carreras']:
        equipo_alumnos, equipo_ayudantes = jugar(equipo_alumnos, equipo_ayudantes, ronda)

    # Esta función imprime el mensaje final según quien haya ganado el challenge.
    anunciar_ganadores(equipo_alumnos, equipo_ayudantes)
