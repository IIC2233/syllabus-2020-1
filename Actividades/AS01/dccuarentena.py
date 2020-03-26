from random import randrange
class DCCuarentena:
    def __init__(self, estudiantes, actividades):
        self.estudiantes = estudiantes
        self.actividades = actividades
        self.usuario_actual = None

    def revisar_identidad(self):
        """
        No modificar este método
        """
        login = True
        while login:
            username = input("Ingresa tu nombre de usuario: ")
            if username in self.estudiantes:
                print(f"¡Hola {username}! Bienvenido a DCCuarentena.\
                	 Recuerda lavarte las manos y no salir de casa.\n")
                self.usuario_actual = self.estudiantes[username]
                login = False
            else:
                print("Intenta nuevamente. \n")

    def sugerir_actividad(self):
        # Acá debes rellenar con un código que sugiera una actividad
        # según el nivel de estres y felicidad.
        # Además, recuerda que el usuario debe realizar la actividad.


        pass

    def opcion(self):
        """
        No modificar este método
        """
        seleccion = input("1. Sugerir actividad \n2. Ingresar otro usuario \n0. Salir\nOpcion: ")
        if seleccion == "1":
            self.sugerir_actividad()
        elif seleccion == "2":
            self.usuario_actual = None
            self.revisar_identidad()
        elif seleccion == "0":
            exit()
        self.opcion()
