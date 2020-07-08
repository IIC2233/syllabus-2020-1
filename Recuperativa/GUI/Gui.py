from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QHBoxLayout,
    QVBoxLayout, QGridLayout, QLabel, QWidget, QPushButton, QSizePolicy,
    QStatusBar
    )
from PyQt5.QtCore import (Qt, pyqtSignal, QSize)
from PyQt5.QtGui import (QBrush, QColor, QPainter, QPalette, QIcon)
from PyQt5 import uic

from GUI import parametros_gui as pg
import os
import sys


class MiVentana(QMainWindow):

    signal_manejar_modulo = pyqtSignal(dict)
    signal_pedir_fiiltro = pyqtSignal(dict)
    signal_eliminar_fiiltro = pyqtSignal()
    signal_agregar_curso = pyqtSignal(dict)
    signal_eliminar_curso = pyqtSignal(dict)
    signal_buscar_cursos_compatibles = pyqtSignal()
    signal_cambio_semestre = pyqtSignal(str)

    def __init__(self):
        super(MiVentana, self).__init__()
        uic.loadUi(os.path.join('GUI', 'mainWindow.ui'), self)

        # Conexión de botones
        self.searchCoursesButton.clicked.connect(self.manejar_aplicar_filtro)
        self.resetFormButton.clicked.connect(self.signal_eliminar_fiiltro.emit)
        self.resetFormButton.clicked.connect(self.limpiar_filtro)
        self.myCoursesListWidget.itemClicked.connect(
            self.eliminar_curso_seleccionado
            )
        self.findCompatibleCourses.clicked.connect(
            self.buscar_cursos_compatible
            )

        # Conexion Combo Box
        self.semesterComboBox.currentTextChanged.connect(self.cambio_semestre)

        # Ajustes que no se lograron en QtDesigner
        self.agregar_assets()
        self.ajustar_tablas()
        self.checkbox_modulos()
        self.horarios_almuerzo()
        self.simbologia_horario()

        self.show()

    def agregar_assets(self):
        '''
        Agrega el icono a la ventana
        '''
        self.setWindowIcon(QIcon(os.path.join(*pg.path_icon)))

    def ajustar_tablas(self):
        '''
        Ajusta el ancho de las columnas de todas las tablas a la ventana
        '''
        for tabla in ('moduleTable', 'scheduleTable', 'resultsTableWidget'):
            header = getattr(self, tabla).horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)

            if tabla == 'resultsTableWidget':
                for i in range(8):
                    if i in (3, 4, 5, 6):
                        continue
                    header.setSectionResizeMode(
                        i, QHeaderView.ResizeToContents
                        )
            else:
                header = getattr(self, tabla).verticalHeader()
                header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def horarios_almuerzo(self):
        '''
        Agrega la celda "Almuerzo" a las tablas
        '''
        for tabla in ('moduleTable', 'scheduleTable'):
            getattr(self, tabla).setSpan(3, 0, 1, 6)
            horario_almuerza = QTableWidgetItem('Almuerzo')
            horario_almuerza.setTextAlignment(Qt.AlignCenter)
            horario_almuerza.setBackground(
                QBrush(QColor(pg.colores['widget']))
                )
            getattr(self, tabla).setItem(3, 0, horario_almuerza)

    def simbologia_horario(self):
        '''
        Agrega la simbología del horario
        '''
        contador = 0

        for key, name in pg.horario.items():
            layout_simbolo = QHBoxLayout()

            cuadrado = QLabel()
            cuadrado.setFixedSize(10, 10)
            cuadrado.setStyleSheet(f'background: {pg.colores[key]};')
            layout_simbolo.addWidget(cuadrado)

            texto = QLabel(name)
            texto.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
            layout_simbolo.addWidget(texto)

            self.symbologyLayout.addLayout(
                layout_simbolo, contador // 4, contador % 4
                )
            contador += 1

    def checkbox_modulos(self):
        '''
        Agrega checkbox's a la tabla para la selección de módulos
        '''
        for h in range(8):
            if h != 3:
                for d in range(6):
                    item_checkbox = QTableWidgetItem()
                    item_checkbox.setFlags(
                        Qt.ItemIsUserCheckable | Qt.ItemIsEnabled
                        )
                    item_checkbox.setCheckState(Qt.Unchecked)
                    self.moduleTable.setItem(h, d, item_checkbox)

    def limpiar_filtro(self):
        self.acronymLineEdit.clear()
        self.nrcLineEdit.clear()
        self.nameLineEdit.clear()
        self.teacherLineEdit.clear()
        self.vacanciesSpinBox.setValue(0)
        self.prerequisitesLineEdit.clear()
        for r in range(self.moduleTable.rowCount()):
            if r != 3:
                for c in range(self.moduleTable.columnCount()):
                    self.moduleTable.item(r, c).setCheckState(Qt.Unchecked)

    def manejar_aplicar_filtro(self):
        '''
        Obtiene la información de los filtros y la procesa
        '''
        filtros = {
            'Semestre': self.semesterComboBox.currentText(),
            'Sigla': self.acronymLineEdit.text(),
            'NRC': self.nrcLineEdit.text(),
            'Nombre': self.nameLineEdit.text(),
            'Profesor': self.teacherLineEdit.text(),
            'Vacantes disponibles': self.vacanciesSpinBox.value(),
            'Prerrequisito de': self.prerequisitesLineEdit.text(),
            'Modulos': self.filtrar_modulos(),
        }
        self.signal_pedir_fiiltro.emit(filtros)

    def filtrar_modulos(self):
        '''
        Filtra los modulos checkeados
        Les da el formato (día, módulo)
        '''
        modulos = ((r, c)
                   for r in range(self.moduleTable.rowCount())
                   for c in range(self.moduleTable.columnCount()))
        modulos_filtrados = list(filter(
            lambda p:
                p[0] != 3 and
                self.moduleTable.item(*p).checkState() == Qt.Checked,
            modulos
        ))
        modulos_formato = []
        for m, d in modulos_filtrados:
            d = pg.dias_semana[d]
            m = m + 1 if m < 3 else m
            modulos_formato.append((d, m))
        return modulos_formato

    def limpiar_tabla_resultados(self):
        '''
        Limpia el contenido de la tabla de resultados
        '''
        for r in range(self.resultsTableWidget.rowCount()):
            self.resultsTableWidget.removeRow(0)

    def widget_modulo(self, row, column, modules):
        '''
        Genera el widget con todos los modulos del ramo
        '''
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(4, 0, 0, 0)
        for tipo_curso, dias in modules.items():
            if len(dias):
                text = ' '.join((
                    f'{tipo_curso}:', *(f'{d}{h}' for d, h in dias)
                    ))
                item = QLabel(text)
                layout.addWidget(item)
        widget.setLayout(layout)
        widget.setFixedHeight(15 * layout.count())
        self.resultsTableWidget.setCellWidget(row, column, widget)

    def boton_agregar(self, row, column):
        '''
        Genera el botón para agregar ramos y lo conecta
        '''
        widget = QWidget()
        layout = QGridLayout()
        boton_agregar = BotonAgregar(row, '&+', self)
        boton_agregar.clicked.connect(lambda row: self.agregar_curso(row))
        layout.addWidget(boton_agregar)
        layout.setContentsMargins(5, 5, 5, 5)
        widget.setLayout(layout)
        self.resultsTableWidget.setCellWidget(row, column, widget)

    def mostrar_cursos_filtradas(self, data):
        '''
        Muestra los datos en la tabla de resultados
        Agrega y conecta un botón para agregar datos
        '''
        self.limpiar_tabla_resultados()

        for info in data.values():
            for info_sec in info["Secciones"].values():
                row = self.resultsTableWidget.rowCount()
                self.resultsTableWidget.insertRow(row)

                for column, value in enumerate(pg.columnas_tabla_resultados):
                    item = QTableWidgetItem()
                    if value in ('Sigla', 'Nombre'):
                        item.setText(info[value])
                    elif value in ('NRC', 'Seccion', 'Profesor'):
                        item.setText(info_sec[value])
                    elif value == 'Vacantes':
                        item.setText('{0} ({1})'.format(
                                info_sec['Vacantes disponibles'],
                                info_sec['Vacantes totales']
                                ))
                    elif value == 'Modulos':
                        self.widget_modulo(row, column, info_sec[value])
                        continue
                    elif value == 'Agregar':
                        self.boton_agregar(row, column)
                        continue

                    item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    self.resultsTableWidget.setItem(row, column, item)

        header = self.resultsTableWidget.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def agregar_curso(self, row):
        '''
        Busca la sigla y sección de la fila
        La envia al backend
        '''
        self.signal_agregar_curso.emit({
            'Sigla': self.resultsTableWidget.item(row, 1).text(),
            'Seccion': self.resultsTableWidget.item(row, 2).text(),
        })

    def mostrar_cursos_seccionados(self, data):
        '''
        Actualiza la información de Mis Cursos
        '''
        self.myCoursesListWidget.clear()

        cursos = sorted(data.values(), key=lambda dict_curso: (
            dict_curso['Sigla'], dict_curso['Seccion']
            ))
        for dict_curso in cursos:
            self.myCoursesListWidget.addItem(
                '{0} {1} {2}\t{3}'.format(
                    dict_curso['NRC'],
                    dict_curso['Sigla'],
                    dict_curso['Seccion'],
                    dict_curso['Nombre']
                ))

    def eliminar_curso_seleccionado(self, event):
        '''
        Obtiene la información del curso a eliminar
        '''
        datos, _ = event.text().strip().split('\t')
        _, sigla, seccion = datos.split(' ')
        self.signal_eliminar_curso.emit({
            'Sigla': sigla,
            'Seccion': seccion,
        })

    def limpiar_horario(self):
        '''
        Limpia el contenido del horario
        '''
        for r in range(self.scheduleTable.rowCount()):
            if r == 3:
                continue
            for c in range(self.scheduleTable.columnCount()):
                self.scheduleTable.removeCellWidget(r, c)

    def mostrar_horario(self, data):
        '''
        Muestra los ramos en el horario
        '''
        self.limpiar_horario()
        horario = dict()
        cursos = sorted(data.values(), key=lambda dict_curso: (
            dict_curso['Sigla'],
            dict_curso['Seccion']
            ))
        for dict_curso in cursos:
            for tipo_curso, dias in dict_curso['Modulos'].items():
                for dia, modulo in dias:
                    dia = pg.dias_semana.index(dia)
                    modulo = int(modulo)
                    modulo -= 1 if (modulo < 4) else 0

                    if (dia, modulo) not in horario:
                        horario[(dia, modulo)] = QVBoxLayout()
                        horario[(dia, modulo)].setSpacing(0)
                        horario[(dia, modulo)].setContentsMargins(0, 0, 0, 0)

                    widget_curso = QLabel('{0}-{1}'.format(
                        dict_curso['Sigla'],
                        dict_curso['Seccion']
                        ))
                    widget_curso.setAlignment(Qt.AlignCenter)
                    widget_curso.setStyleSheet(
                        f'background: {pg.colores[tipo_curso]};'
                        )
                    horario[(dia, modulo)].addWidget(widget_curso)

        for dm, layout in horario.items():
            dia, modulo = dm
            widget_modulo = QWidget()
            widget_modulo.setLayout(layout)
            widget_modulo.setFixedHeight(23 * layout.count())
            self.scheduleTable.setCellWidget(modulo, dia, widget_modulo)

        header = self.scheduleTable.verticalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def buscar_cursos_compatible(self):
        '''
        Envia la señal para obtener cursos compatibles
        '''
        self.signal_buscar_cursos_compatibles.emit()

    def cambio_semestre(self, semestre):
        self.signal_cambio_semestre.emit(semestre)
        self.limiar_todo()

    def limiar_todo(self):
        self.limpiar_horario()
        self.limpiar_tabla_resultados()
        self.limpiar_filtro()
        self.myCoursesListWidget.clear()


class BotonAgregar(QPushButton):
    '''
    Botón que alamcena información y la envia cuando se le hace click
    '''

    clicked = pyqtSignal(int)

    def __init__(self, row, *args, **kwargs):
        super(QPushButton, self).__init__(*args, **kwargs)
        self.row = row
        self.setFixedSize(20, 20)
        self.setStyleSheet(
            f'''
            background-color: {pg.colores['button']};
            color: white;
            '''
            )

    def mouseReleaseEvent(self, ev):
        self.clicked.emit(self.row)


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    window = MiVentana()
    app.exec_()
