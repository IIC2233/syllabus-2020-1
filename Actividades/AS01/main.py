"""
        No modificar este módulo
"""

from cargar import cargar_actividades, cargar_estudiantes
from dccuarentena import DCCuarentena

# Con esta función cargamos el diccionario de estudiantes
estudiantes = cargar_estudiantes("estudiantes.csv")
# Con esta función cargamos el diccionario de actividades
actividades = cargar_actividades("actividades.csv")



# Instanciamos DCCuarentena, junto con sus argumentos 
dccuarentena = DCCuarentena(estudiantes, actividades)
while True:
    # Para empezar, revisamos la identidad del usuario
    dccuarentena.revisar_identidad()

    # Si tenemos un usuario actual, le damos opciones
    if dccuarentena.usuario_actual:
        dccuarentena.opcion()
