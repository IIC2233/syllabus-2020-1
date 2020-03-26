from estudiantes import Alumno, Ayudante
from actividades import Hobby, Deber
from collections import defaultdict
import random


def cargar_estudiantes(ruta_archivo_estudiantes):
    """ No modificar esta parte """
    estudiantes = defaultdict(lambda: "El usuario no existe")
    with open(ruta_archivo_estudiantes, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            # Las separamos por coma y los tenemos como variables
            tipo, username, hobbies, deberes = line.strip().split(";")
            hobbies = hobbies.split(",")
            deberes = deberes.split(",")
            """
            COMIENZA A MODIFICAR DESDE ACÁ
            Aquí debes instanciar a los alumnos y estudiantes.
            Además, debes guardarlos en el defaultdict estudiantes,
            con el formato username:instancia
            """


        return estudiantes

def cargar_actividades(ruta_archivo_actividades):
    """ No modificar esta parte """
    actividades = dict()
    with open(ruta_archivo_actividades, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            # Las separamos por coma y lo tenemos como variable
            tipo, nombre, felicidad, estres = line.strip().split(";")
            felicidad = int(felicidad)
            estres = int(estres)
            """
            COMIENZA A MODIFICAR DESDE ACÁ
            Debes instanciar las actividades acá.
            Además, debes guardarlas en el dict actividades,
            en el formato nombre:instancia
            """

        
        return actividades



#################### NO MODIFICAR ############################


def revisar_progreso(tipo_de_avance, dict):
    if tipo_de_avance == "solo_formato":
        key, value = random.choice(list(dict.items()))
        print(f"""Tu diccionario tiene el siguiente formato:
{key}: {value.__repr__}""")
    elif tipo_de_avance == "ver clases":
        list_dict = list(dict.items())
        clases = []
        for key, value in list_dict:

            if len(clases) == 1 and (type(clases[0]) != type(value)):

                clases.append(value)
                break
            elif not clases:

                clases.append(value)

        for clase in clases:
            print(100*"-")
            print(f"""
Tu clase {type(clase).__name__} tiene los siguientes atributos:
""")
            properties = False
            for attr in clase.__dict__.keys():
                print(attr)
                if attr == "_felicidad" or attr == "_estres":
                    properties = True
            if properties:
                print(f"""
Muy bien, ahora probemos tus properties:

{type(clase).__name__}.felicidad -> 0
{type(clase).__name__}.felicidad += 1000""")
                clase._felicidad = 0
                clase.felicidad += 1000
                print(f"""{type(clase).__name__}.felicidad -> {clase._felicidad}""")

                print(f"""{type(clase).__name__}.felicidad -> 0
{type(clase).__name__}.felicidad -= 1000""")
                clase._felicidad = 0
                clase.felicidad -= 1000
                print(f"""{type(clase).__name__}.felicidad -> {clase._felicidad}""")

                print(f"""{type(clase).__name__}.felicidad -> 0
{type(clase).__name__}.felicidad += 10""")
                clase._felicidad = 0
                clase.felicidad += 10
                print(f"""{type(clase).__name__}.felicidad -> {clase._felicidad}""")

                print(f"""
{type(clase).__name__}.estres -> 0
{type(clase).__name__}.estres += 1000""")
                clase._estres = 0
                clase.estres += 1000
                print(f"""{type(clase).__name__}.estres -> {clase._estres}""")

                print(f"""{type(clase).__name__}.estres -> 0
{type(clase).__name__}.estres -= 1000""")
                clase._estres = 0
                clase.estres -= 1000
                print(f"""{type(clase).__name__}.estres -> {clase._estres}""")

                print(f"""{type(clase).__name__}.estres -> 0
{type(clase).__name__}.estres += 10""")
                clase._estres = 0
                clase.estres += 10
                print(f"""{type(clase).__name__}.estres -> {clase._estres}""")


if __name__ == '__main__':
    estudiantes = cargar_estudiantes("estudiantes.csv")
    revisar_progreso("solo_formato", estudiantes)
    revisar_progreso("ver clases", estudiantes)
    actividades = cargar_actividades("actividades.csv")
    revisar_progreso("solo_formato", actividades)
    revisar_progreso("ver clases", actividades)
