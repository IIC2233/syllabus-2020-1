from random import choice

from PyQt5.QtCore import QObject, pyqtSignal

from parametros import dic_infanteria, dic_artilleria, dic_rango


class Logica(QObject):  

    senal_resultado_verificacion = pyqtSignal(bool)
    senal_comenzar_juego = pyqtSignal(dict)
    senal_enviar_resultado_ronda = pyqtSignal(dict)
    orden_de_superioridad = {
        'Infanteria': 'Rango',
        'Rango': 'Artilleria',
        'Artilleria': 'Infanteria'
    }
    
    def __init__(self):
        super().__init__()

    def verificar_nombre(self, nombre):
        if not nombre.isalnum():
            self.senal_resultado_verificacion.emit(True)
        else:
            self.usuario = nombre
            self.senal_resultado_verificacion.emit(False)
            self.comenzar_juego()

    def comenzar_juego(self):
        self.victorias = 0
        self.derrotas = 0
        infanteria, rango, artilleria = self.elegir_cartas_aleatorias()
        data = {
            'usuario': self.usuario,
            'victorias': self.victorias,
            'derrotas': self.derrotas,
            'infanteria': infanteria,
            'rango': rango,
            'artilleria': artilleria
        }
        self.senal_comenzar_juego.emit(data)

    def elegir_cartas_aleatorias(self):
        carta_infanteria = choice(list(dic_infanteria.values()))
        carta_rango = choice(list(dic_rango.values()))
        carta_artilleria = choice(list(dic_artilleria.values()))
        return carta_infanteria, carta_rango, carta_artilleria

    def jugar_carta(self, carta_usuario):
        carta_enemiga = choice(self.elegir_cartas_aleatorias())
        tipo_usuario = carta_usuario["tipo"]
        tipo_enemigo = carta_enemiga["tipo"]

        if tipo_usuario == tipo_enemigo:
            valor_usuario = carta_usuario["valor"]
            valor_enemigo = carta_enemiga["valor"]
            if valor_enemigo > valor_usuario:
                mensaje = '¡Perdiste la ronda!'
                self.derrotas += 1
            elif valor_enemigo < valor_usuario:
                mensaje = '¡Ganaste la ronda!'
                self.victorias += 1
            elif valor_enemigo == valor_usuario:
                mensaje = '¡Empate en la ronda!'
        else:
            if self.orden_de_superioridad[tipo_enemigo] == tipo_usuario:
                mensaje = '¡Perdiste la ronda!'
                self.derrotas += 1
            else:
                mensaje = '¡Ganaste la ronda!'
                self.victorias += 1

        self.enviar_resultado(carta_usuario, carta_enemiga, mensaje)

    def enviar_resultado(self, carta_usuario, carta_enemiga, mensaje):
        infanteria, rango, artilleria = self.elegir_cartas_aleatorias()
        data = {
            'usuario': self.usuario,
            'victorias': self.victorias,
            'derrotas': self.derrotas,
            'infanteria': infanteria,
            'rango': rango,
            'artilleria': artilleria,
            'jugador': carta_usuario,
            'enemigo': carta_enemiga,
            'mensaje': mensaje,
            'resultado': 'pendiente'
        }
        if self.victorias >= 4:
            data['resultado'] = 'victoria'
        elif self.derrotas >= 4:
            data['resultado'] = 'derrota'
        self.senal_enviar_resultado_ronda.emit(data)
    
