from GUI.Gui import MiVentana
from DCCursos import DCCursos

from PyQt5.QtWidgets import QApplication
import sys


def hook(type, value, traceback):
    print(type)
    print(traceback)


sys.__excepthook__ = hook
app = QApplication(sys.argv)

my_window = MiVentana()
dccursos = DCCursos()

# --------------- SEÑALES ---------------
my_window.signal_pedir_fiiltro.connect(dccursos.aplicar_filtro)
my_window.signal_eliminar_fiiltro.connect(dccursos.eleminar_filtro)
my_window.signal_agregar_curso.connect(dccursos.agregar_curso)
my_window.signal_eliminar_curso.connect(dccursos.eliminar_curso)
my_window.signal_buscar_cursos_compatibles.connect(dccursos.cursos_compatibles)

dccursos.signal_mostrar_cursos_filtrados.connect(my_window.mostrar_cursos_filtradas)
dccursos.signal_limpiar_filtros.connect(my_window.limpiar_tabla_resultados)
dccursos.signal_mostrar_cursos_seleccionadas.connect(my_window.mostrar_cursos_seccionados)
dccursos.signal_mostrar_cursos_seleccionadas.connect(my_window.mostrar_horario)

app.exec_()
