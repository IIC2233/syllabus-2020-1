from abc import ABC, abstractmethod
import random


class Jugador(ABC):

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar
        pass

    def __str__(self):
        if self.equipo == 'ayudante':
            return f'Ayudante {self.nombre} ({self.especialidad})'
        return f'Alumno(a) {self.nombre} ({self.especialidad})'
    
    def __repr__(self):
        return (f'({type(self).__name__}) {self.nombre}: '
                f'equipo={self.equipo}|'
                f'energia={self.energia}|'
                f'inteligencia={self.inteligencia}|'
                f'audacia={self.audacia}|'
                f'trampa={self.trampa}|'
                f'nerviosismo={self.nerviosismo}')

    @abstractmethod
    def enfrentar(self, tipo_de_juego, enemigo):
        # Completar
        pass


# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorMesa:

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        pass

    def jugar_mesa(self, enemigo):
        # Completar
        pass




# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCartas:

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        pass


    def jugar_cartas(self, enemigo):
        # Completar
        pass



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCombate:

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        pass


    def jugar_combate(self, enemigo):
        # Completar
        pass



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCarreras:

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        pass


    def jugar_carrera(self, enemigo):
        # Completar
        pass



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorInteligente:

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        pass



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorIntrepido:

    def __init__(self, nombre, equipo, especialidad, energia):
        # Completar 
        # ¡Aprovecha herencia!
        pass
