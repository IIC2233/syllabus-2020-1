import json
from collections import defaultdict
from cargar_cursos import cargar_cursos

### Espacio para funciones auxiliares ###


### --------------------------------- ###


def filtrar_por_prerrequisitos(curso, dicc_de_cursos):

    # Completar

    pass


def filtrar_por_cupos(cupos, dicc_de_cursos):

    # Completar

    pass


def filtrar_por(llave, string, dicc_de_cursos):
    '''
    llave puede ser 'Nombre', 'Profesor', 'NRC' o 'Sigla'
    '''

    # Completar

    pass


def filtrar_por_modulos(modulos_deseados, dicc_de_cursos):

    # Completar

    pass


def filtrar_por_cursos_compatibles(lista_nrc, dicc_de_cursos):

    # Completar

    pass


if __name__ == "__main__":

    semestre = "2020-1"
    cursos = cargar_cursos(semestre)

    # Filtrar por Prerrequisitos
    # avanzada = cursos['IIC2233']
    # for sigla, info_curso in filtrar_por_prerrequisitos(avanzada, cursos).items():
    #     print(sigla, info_curso)

    # Filtar por Cupos
    # for sigla, info_curso in filtrar_por_cupos(25, cursos).items():
    #     for nr_seccion, info_seccion in info_curso['Secciones'].items():
    #         print(sigla, nr_seccion, info_seccion['Vacantes disponibles'])

    # Filtrar por Profesor
    # resultado = filtrar_por('Profesor', 'cris', cursos)
    # for sigla, info_curso in resultado.items():
    #     for info_seccion in info_curso['Secciones'].values():
    #         print(info_seccion['Profesor'])

    # Filtrar por Sigla
    # resultado = filtrar_por('Sigla', 'iic2', cursos)
    # for sigla, info_curso in resultado.items():
    #     print(sigla)

    # Filtrar por NRC
    # resultado = filtrar_por('NRC', '211', cursos)
    # for sigla, info_curso in resultado.items():
    #     for info_seccion in info_curso['Secciones'].values():
    #         print(info_seccion['NRC'])

    # Filtrar por Nombre
    # resultado = filtrar_por('Nombre', 'cri', cursos)
    # for sigla, info_curso in resultado.items():
    #     print(info_curso['Nombre'])

    # Filtar por Modulo
    # for sigla, info_curso in filtrar_por_modulos([('J',5), ('V', 5)], cursos).items():
    #     for nr_seccion, info_seccion in info_curso['Secciones'].items():
    #         print(sigla, nr_seccion, info_seccion['Modulos'])

    # Filtar por horarios
    # for sigla, info_curso in filtrar_por_cursos_compatibles(['10732', '10791', '21116', '15169', '10923', '18871', '23685', '10892', '10660', '10881'], cursos).items():
    #     for nr_seccion, info_seccion in info_curso['Secciones'].items():
    #         print(sigla, info_seccion['NRC'], info_seccion['Modulos'])

    