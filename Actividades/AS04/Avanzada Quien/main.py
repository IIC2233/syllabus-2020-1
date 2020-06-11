from PyQt5.QtWidgets import QApplication
from logica import AdivinaQuien
from ventanas import VentanaPrincipal
import sys

if __name__ == "__main__":
    app = QApplication([])
    backend = AdivinaQuien()
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    ventana_principal.senal_enviar_info.connect(backend.revisar_usuario)
    backend.senal_revelar.connect(ventana_principal.revelar)

    sys.exit(app.exec_())