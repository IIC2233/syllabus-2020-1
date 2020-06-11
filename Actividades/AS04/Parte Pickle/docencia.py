from decodificador_docencia import cargar_instancia, guardar_instancia, Ayudante
from decodificador_docencia import AyudanteJefe, EquipoDocencia
import sys
import os
import traceback
import pickle


def chequeo_estado_ayudantes_docente(objeto_ayudantes):
    for ayudante in objeto_ayudantes.ayudantes_normales:
        if ayudante.cargo == "Jefe":
            print("El ayudante jefe todavía se encuentra en la lista de ayudantes normales")
            return False
    if objeto_ayudantes.ayudante_jefe is None:
        print("El ayudante jefe no está asignado a self.ayudante_jefe de EquipoDocencia")
        return False
    return True


def chequeo_estado_ayudante_jefe(objeto_ayudante_jefe):
    if objeto_ayudante_jefe.pizza_favorita != None:
        print("El atributo pizza_favorita es diferente a None")
        return False
    if objeto_ayudante_jefe.trabajo_restante != "Nada":
        print("El atributo trabajo_restante es diferente a Nada")
        return False
    if objeto_ayudante_jefe.experto != "TortugaNinja":
        print("El atributo experto es diferente a TortugaNinja")
        return False
    if objeto_ayudante_jefe.cargo != "Jefe":
        print("El atributo cargo el diferente a Jefe")
        return False
    if objeto_ayudante_jefe.usuario_github != "drpinto1":
        print("El atributo github_user el diferente a drpinto1")
        return False
    if objeto_ayudante_jefe.pokemon_favorito != "umbreon":
        print("El atributo pokemon_favorito el diferente a umbreon")
        return False
    if objeto_ayudante_jefe.carrera != "Astronomia":
        print("El atributo carrera el diferente a Astronomia")
        return False
    return True


if __name__ == "__main__":

    print("--------------Parte Pickle de la actividad-------------")
    try:
        # Se carga el archivo con la instancia de la clase EquipoDocencia
        ayudantes_todo = cargar_instancia("equipo_docencia.bin")

        # Se hace chequeo de la instancia de la clase EquipoDocencia
        if chequeo_estado_ayudantes_docente(ayudantes_todo):
            print("El estado de EquipoDocencia es el que corresponde")

            # Se hace el chequeo de la instancia AyudanteJefe
            ayudante_jefe = ayudantes_todo.ayudante_jefe
            jefe_serializado = pickle.dumps(ayudante_jefe)
            jefe_deserializado = pickle.loads(jefe_serializado)
            if chequeo_estado_ayudante_jefe(jefe_deserializado):
                print("El estado de AyudanteJefe es el adecuado")
                # Guardamos la clase EquipoDocencia
                if guardar_instancia("equipo_corregido.bin", ayudantes_todo):
                    usuario = jefe_deserializado.usuario_github
                    parte_1 = jefe_deserializado.carrera
                    parte_2 = jefe_deserializado.pokemon_favorito
                    print(f"El usuario para el jefe de docencia es: {usuario}")
                    print(f"La contreseña para el jefe de docencia es: {parte_1}+{parte_2}")
                else:
                    print("No has retornado True al guardar la instancia")
            else:
                print("EL objeto AyudanteJefe no cumple con lo solicitado")
        else:
            print("La clase EquipoDocencia no tiene el estado requerido")
    except Exception as error:
        nombre_archivo = "decodificador_docencia.py"
        print("Este mensaje te dará un poco de información de tu error:")
        print(f"No haz iniciado esta parte o tuvo un error y habría dejado de funcionar.")
        print(f"Recuerda, TODO error comienza en el archivo {nombre_archivo}, no en docencia.py.")
        print(f"Los datos del error: {traceback.format_exc()}")

    print("----------Fin Parte Pickle de la actividad-------------")
