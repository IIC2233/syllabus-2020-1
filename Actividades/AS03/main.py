import os

from cargar_tweets import cargar_tweets
from doomsday_clock import DoomsdayClock
from lideres import Hacker, LiderMundial
from parametros import ENOJO_INICIAL, TIEMPO_INICIAL, VELOCIDAD_INICIAL


class Simulacion:

    def __init__(self, tweets_pinto, tweets_trumpzini):
        self.doomsday_clock = DoomsdayClock(VELOCIDAD_INICIAL, TIEMPO_INICIAL)
        self.dr_pinto = LiderMundial("Dr. Pin Tong-Un", tweets_pinto, ENOJO_INICIAL, self.doomsday_clock)
        self.trumpzini = LiderMundial("Trumpzini", tweets_trumpzini, ENOJO_INICIAL, self.doomsday_clock)
        # Implementar bonus a continuación

    def comenzar(self):
        print("INICIANDO SIMULACIÓN...")
        # Completar
        pass


if __name__ == "__main__":
    # No modificar
    tweets_pinto = cargar_tweets(os.path.join("datos", "pin_tweets.csv"))
    tweets_trumpzini = cargar_tweets(os.path.join("datos", "trumpzini_tweets.csv"))

    simulacion = Simulacion(tweets_pinto, tweets_trumpzini)
    simulacion.comenzar()
