from  PyQt5.QtWidgets import QApplication

from classes import RickSanchez, Morty, AI
from main_window import MainWindow
from inicial_window import InicialWindow
import sys
import time


app = QApplication([])

inicial_window_1 = InicialWindow()
window = MainWindow()
rick = RickSanchez(window.display_x, window.display_y)
ai = AI(window.display_x, window.display_y)

# Conectamos ambas ventanas mediante esta señal
inicial_window_1.senal_iniciar_juego.connect(window.iniciar_ventana)

#Conectamos la ventana principal con el backend
window.start_game_signal.connect(ai.begin)
window.move_character_signal.connect(rick.move)
window.shoot_signal.connect(rick.shoot)

rick.create_syringer_signal.connect(window.create_syringer)
rick.update_position_signal.connect(window.update_position)
rick.check_shoot_signal.connect(ai.check_shoot)

ai.arrow_impacted_signal.connect(rick.impact_syringer)
ai.end_game_signal.connect(window.close)
ai.create_morty_signal.connect(window.create_morty)
ai.update_position_signal.connect(window.update_position)

# Mostramos la ventana inicial
inicial_window_1.show() 
sys.exit(app.exec_())
