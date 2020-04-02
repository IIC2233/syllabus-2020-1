import random 

# La siguiente función elige aleatoriamente a un competidor del equipo que
# sea de la especialidad pedida.
def elegir_jugador(tipo_de_juego, equipo):
    candidatos = equipo[tipo_de_juego]
    return random.choice(candidatos)


def jugar(equipo_alumnos, equipo_ayudantes, tipo_de_juego):

    # Primero se separan los competidores y el puntaje,
    # asignándolos a las siguientes variables
    alumnos, puntaje_alumnos = equipo_alumnos
    ayudantes, puntaje_ayudantes = equipo_ayudantes
    print('Los puntajes actuales son:\n'
          f'Alumnos:   {puntaje_alumnos} puntos\n'
          f'Ayudantes: {puntaje_ayudantes} puntos\n')

    # Se asignan los competidores por equipo
    alumno_a_jugar = elegir_jugador(tipo_de_juego, alumnos)
    ayudante_a_jugar = elegir_jugador(tipo_de_juego, ayudantes)

    # Se procede al enfrentamiento, el cual varía según el tipo de juego.
    # Esto retorna un boolean que determina la asignación de puntaje.
    if alumno_a_jugar.enfrentar(tipo_de_juego, ayudante_a_jugar):
        print(f'¡{alumno_a_jugar} ha vencido! Punto para los alumnos\n')
        puntaje_alumnos += 1
    else:
        print(f'¡{ayudante_a_jugar} ha vencido! Punto para los ayudantes\n')
        puntaje_ayudantes += 1

    # Se vuelven a formar las tuplas, ahora con el puntaje actualizado.
    equipo_alumnos = (alumnos, puntaje_alumnos)
    equipo_ayudantes = (alumnos, puntaje_ayudantes)
    
    return equipo_alumnos, equipo_ayudantes


# Esta función se activa luego de que se terminan las rondas
# e imprime los resultados finales del challenge
def anunciar_ganadores(equipo_alumnos, equipo_ayudantes):

    # Se asignan los valores de la tuplas a variables.
    alumnos, puntaje_alumnos = equipo_alumnos
    ayudantes, puntaje_ayudantes = equipo_ayudantes

    # Se comparan los puntajes.
    if puntaje_alumnos > puntaje_ayudantes:
        print(f'¡Los alumnos han ganado las Olimpiadas con un puntaje de {puntaje_alumnos}!')
    elif puntaje_alumnos < puntaje_ayudantes:
        print(f'¡Los ayudantes han ganado las Olimpiadas con un puntaje de {puntaje_ayudantes}!')
    elif puntaje_alumnos == puntaje_ayudantes:
        print('¡Ha habido un empate entre alumnos y ayudantes!')