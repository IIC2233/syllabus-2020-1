from collections import namedtuple
import os

def cargar_comunas_en_cuarentena(path):
    comunas = []
    with open(path, 'r', encoding="utf-8") as file
        for line in file.readlines():
            comuna = line.strip()
            comunas.append(comuna)
    return comunas

def cargar_clave_unica(path):
    solicitantes = []
    with open(path, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            persona = line.strip()
            solicitantes.append(persona)
    print(solicitantes[len(solicitantes)]) #esta línea no es necesaria
    return solicitantes

def cargar_datos(path):
    datos_registrados = dict()
    persona = namedtuple("Persona", ["rut", "nombre", "clave", "domicilio"])
    with open(path, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            # Las separamos por coma
            rut, nombre, clave, domicilio = line.strip().split(',')
            datos_registrados[rut] = persona(rut, nombre, clave, domicilio)
    return datos_registrados


def cargar_permiso_hora(path):
    permisos = dict()
    permiso = namedtuple("PermisoHora", ["rut", "hora"])
    with open(path, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            # Las separamos por coma
            rut, hora = line.strip().split('')
            permisos[rut] = permiso(rut, hora)
    return permisos

def cargar_permiso_supermercado(path):
    permisos = dict()
    permiso = namedtuple("PermisoSupermercado", ["rut", "salida", "llegada"])
    with open(path, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            # Las separamos por coma
            rut, salida, llegada = line.strip().split(',')
            permisos[rut] = permis(rut, salida, llegada)
    return permisos


if __name__ == "__main__":
    # Probar cargar_comunas_en_cuarentena
    cargar_comunas_en_cuarentena(os.path.join("datos", 'cuarentena.csv'))

    # Probar cargar_comunas_en_cuarentena
    cargar_clave_unica(os.path.join("datos", 'ruts_clave_unica.csv'))

    # Probar cargar_datos
    cargar_datos(os.path.join("datos", 'datos.csv'))

    # Probar cargar_permiso_hora
    cargar_permiso_hora(os.path.join("datos", 'permiso_hora.csv'))

    # Probar cargar_permiso_supermercado
    cargar_permiso_supermercado(os.path.join("datos", 'permiso_supermercado.csv'))

    print("--------------------------")
    print('Todo está bajo control! Puedes continuar con la actividad :)')
    print("--------------------------")
