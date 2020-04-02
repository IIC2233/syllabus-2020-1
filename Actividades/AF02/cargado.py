import jugadores

def cargar_jugadores():
    tipos_de_juego = ['mesa', 'cartas', 'combate', 'carreras']

    # El siguiente diccionario relaciona las especialidades con sus respectivas clases.
    clases_por_especialidad = {
        'mesa': jugadores.JugadorMesa,
        'cartas': jugadores.JugadorCartas,
        'combate': jugadores.JugadorCombate,
        'carreras': jugadores.JugadorCarreras,
        'intrepido': jugadores.JugadorIntrepido,
        'inteligente': jugadores.JugadorInteligente
    }

    # Las siguientes iteraciones crean un diccionario
    # donde cada especialidad es una llave que tienen como valor una lista vacía,
    # a las que posteriormente se les agregaran los
    # competidores correspondientes a esa especialidad.
    dicc_equipo_alumnos = {especialidad: [] for especialidad in tipos_de_juego}
    dicc_equipo_ayudantes = {especialidad: [] for especialidad in tipos_de_juego}

    # Se abre el archivo
    with open('db_af02.csv', 'rt', encoding='utf-8') as archivo_competidores:
        # Se lee el archivo y se guarda cada línea en una lista,
        # menos la primera línea que es el encabezado de las columnas de la base de datos,
        # el resto son los datos de cada competidor.
        lineas_contrincantes = archivo_competidores.readlines()[1:]

    # A continuación se carga cada competidor.
    for linea in lineas_contrincantes:
        # Se separan los datos del competidor en una lista.
        atributos = linea.strip().split(',')
        # Se extrae la especialidad el competidor.
        especialidad = atributos[2]
        # Se asigna la clase según la especialidad.
        Clase = clases_por_especialidad[especialidad]
        # Se instancia la clase.
        competidor = Clase(*atributos) 

        # Se revisa que la instancia contenga los atributos mínimos pedidos.
        for atributo in ['equipo', 'energia', 'inteligencia', 'audacia', 'trampa', 'nerviosismo']:
            if not hasattr(competidor, atributo):
                print(f"Instancia {Clase.__name__} no contiene atributo: {atributo}")

        # Ahora se asigna cada competidor al equipo que corresponde y a su especialidad.
        if competidor.equipo == 'alumno':
            if especialidad in tipos_de_juego:
                dicc_equipo_alumnos[especialidad].append(competidor)
            elif especialidad == 'intrepido':
                dicc_equipo_alumnos['combate'].append(competidor)
                dicc_equipo_alumnos['carreras'].append(competidor)
            elif especialidad == 'inteligente':
                dicc_equipo_alumnos['mesa'].append(competidor)
                dicc_equipo_alumnos['cartas'].append(competidor)
        elif competidor.equipo == 'ayudante':
            if especialidad in tipos_de_juego:
                dicc_equipo_ayudantes[especialidad].append(competidor)
            elif especialidad == 'intrepido':
                dicc_equipo_ayudantes['combate'].append(competidor)
                dicc_equipo_ayudantes['carreras'].append(competidor)
            elif especialidad == 'inteligente':
                dicc_equipo_ayudantes['mesa'].append(competidor)
                dicc_equipo_ayudantes['cartas'].append(competidor)
    return dicc_equipo_alumnos, dicc_equipo_ayudantes


# Esta función imprime los equipos y sus jugadores por especialidad.
def imprimir_equipos(alumnos, ayudantes):
    print("Instancias cargadas:")
    print("Alumnos:")
    for tipo in alumnos:
        print(f"Juego tipo: {tipo}")
        for alumno in alumnos[tipo]:
            print(repr(alumno))
    print("Ayudantes:")
    for tipo in ayudantes:
        print(f"Juego tipo: {tipo}")
        for ayudante in ayudantes[tipo]:
            print(repr(ayudante))
    print()