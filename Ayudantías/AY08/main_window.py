import sys
import random
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.QtCore as core
from PyQt5 import uic


#Usamos la función loadUiType para generar una tupla del nombre de la ventana y su clase base
window_name, base_class = uic.loadUiType("MainWindow.ui")


class MainWindow(window_name, base_class):

	# Creamos las señales de disparar jeringa y mover Rick
    start_game_signal = core.pyqtSignal(bool)
    move_character_signal = core.pyqtSignal(str)
    shoot_signal = core.pyqtSignal() 

    def __init__(self):
        super().__init__()
        self._frame = 1 # Esto será usado para hacer movimientos fluidos en los sprites
        self.display_y = 560
        self.display_x = 720
        self.setupUi(self) #Contrusimos la ventana creada en QtDesigner

        # Agregamos los tiles a nuestra Grilla
        self.characters = dict()
        for i in range(self.display_y//16):
            for j in range(self.display_x//16):
                if j == 0:
                    if i > (self.display_y//16)//1.4:
                        pixmap = gui.QPixmap("sprites/map/edge_1b.png")
                    else:
                        pixmap = gui.QPixmap("sprites/map/edge_1.png")                    
                elif j == self.display_x//16 - 1:
                    if i > (self.display_y//16)//1.4:
                        pixmap = gui.QPixmap("sprites/map/edge_2b.png")
                    else:
                        pixmap = gui.QPixmap("sprites/map/edge_2.png")                                   
                elif i > (self.display_y//16)//1.4:
                    pixmap = gui.QPixmap("sprites/map/road_2.png")
                else:
                    pixmap = gui.QPixmap("sprites/map/road.png")
                sec = widgets.QLabel()
                sec.setPixmap(pixmap)
                self.MainGrid.addWidget(sec, i, j)
        self.rick_label.raise_() # Con raise_(), enviamos este widget al frente
        self.characters['doc'] = self.rick_label # Guardamos el label con nuestras entidades

    def iniciar_ventana(self, ususario):
        self.usuario_label.setText('Usuario: ' + ususario)
        self.start_game_signal.emit(True)
        self.show()

        
        # Llamamos los metodos conectados en setupUi
    def move_left_clicked(self, event): 
        self.move_character_signal.emit('L')

    def move_right_clicked(self, event):
        self.move_character_signal.emit('R')

    def shoot_clicked(self, event):
        self.shoot_signal.emit()

    def salir(self, event):
        sys.exit()


        # Ahora lo hacemos para las teclas
    def keyPressEvent(self, event):
        if event.key() in [core.Qt.Key_A]:
            self.move_character_signal.emit('L')
        elif event.key() in [core.Qt.Key_D]:
            self.move_character_signal.emit('R')
        elif event.key() == core.Qt.Key_W:
            self.shoot_signal.emit()

    def update_position(self, event): # Recibe un dict con el nombre, el sprite (o delete) y la posicion
        char = self.characters[event["char"]]
        if event.get("sprite"):
            pixmap = gui.QPixmap(
                f"sprites/{event['sprite']}_{event['frame']}.png")
            pixmap = pixmap.scaled(32, 32)
            char.setPixmap(pixmap)
        elif event.get("delete"):
            char.setPixmap(gui.QPixmap(None))
            return
        char.move(event['x'], event['y'])
        self.update() 
    
    # Recibimos la posicion del morty
    def create_morty(self, data):
        char = widgets.QLabel(self)
        #creamos el QLabel con el pixmap indicado
        char.setPixmap(
            gui.QPixmap('sprites/morty_1.png').scaled(32, 32))
        char.move(
            data["x"],
            data["y"]
            )
        char.show()
        # mostramos y agregamos el QLabel a nuestras entidades
        self.characters[data["char"]] = char
    


    # Recibimos la posicion de la jeringa
    def create_syringer(self, data):
        char = widgets.QLabel(self)
        #Creamos el QLabel con el pixmap indicado
        char.setPixmap(
            gui.QPixmap('sprites/syringe.png').scaled(20, 30))
        char.move(
            data["x"],
            data["y"]
            )
        char.show()
        # Mostramos y agregamos el QLabel a nuestras entidades
        self.characters[data["char"]] = char



if __name__ == '__main__':
    app = widgets.QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
