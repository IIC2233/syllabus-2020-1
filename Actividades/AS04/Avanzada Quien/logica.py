import os
from PyQt5.QtCore import QObject, pyqtSignal

class AdivinaQuien(QObject):

    senal_revelar = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.datos()
    
    def datos(self):
        ruta_data = os.path.join('data.txt')
        with open(ruta_data, encoding = 'UTF-8') as archivo:
            lineas = archivo.readline()
        text = int(lineas, 2)
        data = text.to_bytes((text.bit_length() + 7) // 8, 'big').decode('UTF-8') or '\0'
        data = data.split(';')
        self.data = [x.split(',') for x in data]

    def revisar_usuario(self, usuario, clave):
        if usuario == self.data[0][0]:
            if clave == self.data[0][1]:
                path = os.path.join('sprites', 'dani.png')
                self.senal_revelar.emit(path, '0')
            else:
                self.senal_revelar.emit(None, 'clave')
        elif usuario == self.data[1][0]:
            if clave == self.data[1][1]:
                path = os.path.join('sprites', 'enzo.png')
                self.senal_revelar.emit(path, '1')
            else:
                self.senal_revelar.emit(None, 'clave')
        elif usuario == self.data[2][0]:
            if clave == self.data[2][1]:
                path = os.path.join('sprites', 'dante.png')
                self.senal_revelar.emit(path, '2')
            else:
                self.senal_revelar.emit(None, 'clave')
        elif usuario == self.data[3][0]:
            if clave == self.data[3][1]:
                path = os.path.join('sprites', 'benja.png')
                self.senal_revelar.emit(path, '3')
            else: 
                self.senal_revelar.emit(None, 'clave')
        else: 
            self.senal_revelar.emit(None, 'usuario')
