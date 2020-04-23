from entidades import Cliente, Producto, IterableOfertones, IteradorOfertones
from funcionalidades import obtener_clientes, categorizar, calcular_precio, generar_productos_disponibles
import os


# Cargar datos

def cargar_encriptados(ruta_clientes):
    clientes = []
    with open(ruta_clientes, "rt", encoding="utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip().split(",")
            linea[2] = linea[2].split(";")
            clientes.append(linea)
    return clientes


def cargar_bonus(ruta_clientes):
    pass


def cargar_productos(ruta_productos):
    productos = {}
    with open(ruta_productos, "rt", encoding="utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip().split(",")
            id_, nombre, categoria, precio, disponible, desc = linea
            productos[id_] = Producto(int(id_), nombre, categoria, int(precio),
                                        disponible == "True", int(desc))
    return productos


if __name__ == "__main__":

    # Se cargan clientes encriptados
    encriptados = cargar_encriptados(os.path.join("data", "clientes_encriptados.csv"))
    # encriptados = cargar_bonus(os.path.join("data", "clientes_encriptados.csv"))

    # Se cargan productos
    productos = cargar_productos(os.path.join("data", "productos.csv"))

    # Obtener clientes desepcriptados
    clientes = obtener_clientes(encriptados)

    if clientes:
        clientes = [Cliente(*i) for i in clientes]
        for cliente in clientes:
            carrito = []
            for ids in cliente.carrito:
                carrito.append(productos[ids])
            cliente.carrito = carrito
        nombres_clientes = [i.nombre for i in clientes]
        print(f"Clientes desencriptados: {nombres_clientes}")
    else:
        clientes = []
        print("obtener_clientes no implementado :c")

    productos = [prod for prod in productos.values()]

    # Categorizar
    print("\n---------- CATEGORIAS ----------\n")
    print(f"Abarrotes: {categorizar(productos, 'abarrotes')}")
    print(f"Frutas: {categorizar(productos, 'frutas')}")
    print(f"Verduras: {categorizar(productos, 'verduras')}")
    print(f"Baño: {categorizar(productos, 'baño')}")
    print(f"Limpieza: {categorizar(productos, 'limpieza')}")
    print(f"Congelados: {categorizar(productos, 'congelados')}")
    print(f"Golosinas: {categorizar(productos, 'golosinas')}")
    print(f"Despensa: {categorizar(productos, 'despensa')}")
    print(f"Líquidos: {categorizar(productos, 'líquidos')}")

    # Calcular precio
    print("\n---------- TOTAL A PAGAR POR CLIENTE ----------\n")
    for cliente in clientes:
        print(f"Cliente: {cliente.nombre}")
        print(f"Total a pagar: {calcular_precio(cliente.carrito)}")

    # Revisar disponbles
    print("\n---------- PRODUCTOS DISPONIBLES PARA CLIENTES ----------\n")
    disponibles = generar_productos_disponibles(clientes)
    if disponibles is None:
        print("Función generar_disponibles retorna None :(")
    else:
        for cliente, producto in disponibles:
            print(f"Producto {producto.nombre} disponible para {cliente.nombre}")

    # Iterable e Iterador Ofertones
    print("\n---------- DESCUENTOS ----------\n")
    ofertones = IterableOfertones(productos)
    iterador_ofertones = iter(ofertones)
    if next(iterador_ofertones):
        iterador_ofertones = iter(ofertones)
        for prod in ofertones:
            print(f"El producto {prod} tiene un {prod.descuento_oferta}% de descuento"
                  f" y está a ${int(prod.precio)}")
    else:
        print("Iterador Ofertones entrega None :c")
