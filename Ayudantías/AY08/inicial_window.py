import PyQt5.QtGui as gui
import PyQt5.QtWidgets as widgets
import PyQt5.QtCore as core
from PyQt5 import uic
import sys


#Usamos la función loadUiType para generar una tupla del nombre de la ventana y su clase base
window_name, base_class = uic.loadUiType("InicialWindow.ui")


class InicialWindow(window_name, base_class):
    #Creamos nuestra señal de usuario
    senal_iniciar_juego = core.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    def iniciar_juego(self):
        # Con este método ya conectado, eviamos la señal conteniendo el usuario y escondemos esta ventana
        self.senal_iniciar_juego.emit(self.lineUsuario.text())
        self.hide()

if __name__ == '__main__':
    app = widgets.QApplication([])
    window = InicialWindow()
    sys.exit(app.exec_())
