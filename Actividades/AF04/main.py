import sys

from PyQt5.QtWidgets import QApplication

from logica import Logica
from ventana_inicial import VentanaInicial
from ventana_principal import VentanaPrincipal, VentanaCombate
from ventana_final import VentanaFinal


if __name__ == "__main__":
    
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    
    # Se genera la aplicación
    a = QApplication(sys.argv)

    # Se instancia back-end principal
    logica_dccuent = Logica()

    # Se instancia la ventana inicial
    ventana_inicial = VentanaInicial()

    # Se conectan las señales de Ventana Inicial y back-end 
    ventana_inicial.senal_revisar_nombre.connect(logica_dccuent.verificar_nombre)
    logica_dccuent.senal_resultado_verificacion.connect(ventana_inicial.recibir_revision)
    
    # Se instancia resto de ventanas
    ventana_principal = VentanaPrincipal()
    ventana_combate = VentanaCombate()
    ventana_final = VentanaFinal()

    # ---- Completa y conecta el resto de las señales aquí...
    logica_dccuent.senal_comenzar_juego.connect(ventana_principal.actualizar)
    
    
    
    # -------------------
    
    ventana_inicial.show()
    sys.exit(a.exec())