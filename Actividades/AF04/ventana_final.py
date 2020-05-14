import sys

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QDir, QUrl
from PyQt5.QtGui import QPixmap, QMovie, QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent,QSound
from PyQt5 import QtMultimedia

from parametros import ruta_victoria, ruta_derrota, ruta_sonido_victoria, ruta_sonido_derrota


class VentanaFinal(QWidget):

    def __init__(self, *args):
        super().__init__(*args)

    def crear_pantalla(self, resultado):
        if resultado == "victoria":
            self.ruta = ruta_victoria
            self.ruta_sonido = ruta_sonido_victoria
            titulo = '¡Victoria!'
        else:
            self.ruta = ruta_derrota
            self.ruta_sonido = ruta_sonido_derrota
            titulo = 'Derrota :('
                        
        self.setWindowTitle(titulo)
        
        self.label_usuario = QLabel()
        self.movie = QMovie(self.ruta)
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()
        
        self.sonido()
        self.show()

    def sonido(self):
        self.soundtrack = QSound(self.ruta_sonido)
        self.soundtrack.play()
        self.soundtrack.setLoops(1000)

    def paintEvent(self, event):
        frame_actual = self.movie.currentPixmap()
        frameRect = frame_actual.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), frame_actual)


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    
    a = QApplication(sys.argv)
    
    print("estoy sonado")
     
    ventana_final = VentanaFinal()
    ventana_final.show()
    
    sys.exit(a.exec())