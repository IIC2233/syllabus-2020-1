class Estudiante:
    # Debes completar el constructor de la clase estudiante
    def __init__(self):

        self.rango_felicidad = tuple()
        self.rango_estres = tuple()

    def realizar_actividad(self, actividad):
        print(f"Realizando {actividad}")
        print(f"El nivel de estres del estudiante es {self.estres}\
             y el de felicidad {self.felicidad}")

    # Debes rellenar las property felicidad
    @property
    def felicidad(self):
        pass

    @felicidad.setter
    def felicidad(self, nueva_felicidad):
        pass

    # Debes rellenar las property estres
    @property
    def estres(self):
        pass

    @estres.setter
    def estres(self, nuevo_estres):
        pass


######## REVISAR LOS PARAMETROS
class Alumno(Estudiante):
    def __init__(self, username, hobbies, deberes):
        # Recuerda iniciar la clase, de manera que herede de Estudiante

        # Definir rangos para alumno

        # Borrar pass cuando lo tengas listo
        pass


    def realizar_actividad(self, actividad):
        print(f"Realizando {actividad}")
        # Debes rellenar esto, para que se ajusten los niveles de felicidad y estres


        # Hasta acá
        print(f"El nivel de estres del estudiante es {self.estres}\
             y el de felicidad {self.felicidad}")


######## REVISAR LOS PARAMETROS
class Ayudante(Estudiante):
    def __init__(self, username, hobbies, deberes):
        # Recuerda iniciar la clase, de manera que herede de Estudiante

        # Definir rangos para Ayudante

        # Borrar pass cuando lo tengas listo
        pass

    def realizar_actividad(self, actividad):
        print(f"Realizando {actividad}")
        # Debes rellenar esto, para que se ajusten los niveles de felicidad y estres


        # Hasta acá
        print(f"El nivel de estres del ayudante es {self.estres}\
             y el de felicidad {self.felicidad}")
