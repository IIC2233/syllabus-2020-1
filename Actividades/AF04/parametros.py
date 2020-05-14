import os

ruta_logo = os.path.join(os.getcwd(), "Sprites" , "logo.png")

ruta_rango = os.path.join(os.getcwd(), "Sprites" , "Ranged")
ruta_infanteria = os.path.join(os.getcwd(), "Sprites" , "Infantry")
ruta_artilleria = os.path.join(os.getcwd(), "Sprites" , "Artillery")

dic_rango = {}
dic_infanteria = {}
dic_artilleria = {}

for image_name in os.listdir(ruta_rango):
    parametros = image_name.split(",")
    nombre = parametros[0]
    valor = int(parametros[1].replace(".png", ""))
    path = os.path.join(os.getcwd(), "Sprites" , "Ranged", image_name)
    dic_rango[nombre] = {"valor": valor, "tipo": "Rango","ruta": path}

for image_name in os.listdir(ruta_infanteria):
    parametros = image_name.split(",")
    nombre = parametros[0]
    valor = int(parametros[1].replace(".png", ""))
    path = os.path.join(os.getcwd(), "Sprites" , "Infantry", image_name)
    dic_infanteria[nombre] = {"valor": valor, "tipo": "Infanteria", "ruta": path}

for image_name in os.listdir(ruta_artilleria):
    parametros = image_name.split(",")
    nombre = parametros[0]
    valor = int(parametros[1].replace(".png", ""))
    path = os.path.join(os.getcwd(), "Sprites" , "Artillery", image_name)
    dic_artilleria[nombre] = {"valor": valor, "tipo": "Artilleria", "ruta": path}

ruta_derrota = os.path.join(os.getcwd(), "Sprites", "Final", "derrota.gif")
ruta_victoria = os.path.join(os.getcwd(), "Sprites", "Final", "victoria.gif")

ruta_sonido_victoria = os.path.join(os.getcwd(), "Sonidos", "victoria.wav")
ruta_sonido_derrota = os.path.join(os.getcwd(), "Sonidos", "derrota.wav")
