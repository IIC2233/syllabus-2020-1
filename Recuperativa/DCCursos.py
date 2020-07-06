from PyQt5.QtCore import pyqtSignal, QObject
import consultas as c
import cargar_cursos as cc


class DCCursos(QObject):

    signal_mostrar_cursos_filtrados = pyqtSignal(dict)
    signal_limpiar_filtros = pyqtSignal()
    signal_mostrar_cursos_seleccionadas = pyqtSignal(dict)

    def __init__(self):
        super(QObject, self).__init__()
        self.cursos = dict()
        self.horario = dict()

    def aplicar_filtro(self, event):
        '''
        Maneja la aplicación de filtros
        '''
        # TODO: conectar con los filtros

        self.cursos = cc.cargar_cursos(event['Semestre'])
        cursos_filtrados = cc.cargar_cursos(event['Semestre'])
        del(event['Semestre'])

        for filtro, valor in event.items():
            if valor:
                if filtro in ('Nombre', 'Profesor', 'NRC', 'Sigla'):
                    cursos_filtrados = c.filtrar_por(
                        filtro, valor, cursos_filtrados
                        )
                elif filtro == 'Vacantes disponibles':
                    cursos_filtrados = c.filtrar_por_cupos(
                        valor, cursos_filtrados
                        )
                elif filtro == 'Modulos':
                    cursos_filtrados = c.filtrar_por_modulos(
                        valor, cursos_filtrados
                        )
                elif filtro == 'Prerrequisito de':
                    curso_de = self.cursos[valor.upper()]
                    cursos_filtrados = c.filtrar_por_prerrequisitos(
                        curso_de, cursos_filtrados
                        )
        else:
            self.signal_mostrar_cursos_filtrados.emit({})

        self.signal_mostrar_cursos_filtrados.emit(cursos_filtrados)

    def eleminar_filtro(self):
        '''
        Elimina los datos filtrados
        '''
        self.cursos_filtradas = None
        self.signal_limpiar_filtros.emit()

    def agregar_curso(self, curso):
        '''
        Agrega un elemento a los ramos seleccionados
        '''
        sigla = curso['Sigla']
        seccion = curso['Seccion']
        nrc = self.cursos[sigla]['Secciones'][seccion]['NRC']

        info_curso = {
            'NRC': nrc,
            'Sigla': sigla,
            'Nombre': self.cursos[sigla]['Nombre'],
            'Seccion': seccion,
            'Modulos': self.cursos[sigla]['Secciones'][seccion]['Modulos']
        }

        self.horario[nrc] = (info_curso)
        self.signal_mostrar_cursos_seleccionadas.emit(self.horario)

    def eliminar_curso(self, curso):
        sigla = curso['Sigla']
        seccion = curso['Seccion']
        nrc = self.cursos[sigla]['Secciones'][seccion]['NRC']

        if nrc in self.horario:
            del(self.horario[nrc])

        self.signal_mostrar_cursos_seleccionadas.emit(self.horario)

    def cursos_compatibles(self):
        nrc_horario = [
            curso['NRC'] for curso in self.horario.values()
        ]

        self.signal_mostrar_cursos_filtrados.emit(
            c.filtrar_por_cursos_compatibles(nrc_horario, self.cursos)
        )
