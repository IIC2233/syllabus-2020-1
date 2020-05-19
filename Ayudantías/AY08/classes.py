import sys
import random
import time
import PyQt5.QtCore as core


class Morty(core.QThread): #Importamos QThread 

    def __init__(self, x, y, _id, speed, waiting): #Creamos los atributos:
                                                        #x, y: determinan las dimensiones de la pantalla
                                                        #_id: para tener una referencia a cada Morty
                                                        #speed: determina la velocidad de Morty
                                                        #waiting: determina el tiempo de espera entre Mortys
        super().__init__()
        self.display_x = x
        self.display_y = y
        self.__x = random.randint(20, x - 52) #Determinamos la posicion x incial
        self.__y = -33 #Determinamos la posicion y inicial
        self.points = 0
        self.alive = True #Booleano que determina si Morty esta vivo
        self.cured = False #Booleano que determina si Morty esta infectado
        self.speed = speed 
        self.waiting = waiting
        self._id = _id
        self.__frame = 0 #Determinamos el frame inicial
        self.update_position_signal = None #Creamos un atributo donde se guardara la señal entregada por la A.I.
    
    @property #Frame es una property ya que debemos iterar entre los 3 sprites de Morty
    def frame(self):
        return self.__frame

    @frame.setter #Con el setter verificamos que frame tome valores entre 0 y 2 (incluidos)
    def frame(self, value):
        if 2 < value:
            self.__frame = 0
        else:
            self.__frame = value
    
    @property #x es una property ya que necesitamos que esta no exeda los limites de la pantalla (display) y donde se envia la señal al frontend (MainWindow)
    def x(self):
        return self.__x

    @x.setter #Con el setter verificamos que x tome valores entre -40 y self.display_x - 48 (no icluidos)
    def x(self, value):
        if -40 < value < self.display_x - 48:
            self.__x = value
            self.update_position_signal.emit( #Emitimos una señal hacia el MainWindow para que se updatee el frontend de Morty (QLabel y QPixmap)
                {'char': self._id,
                 'x': self.x,
                 'y': self.y,
                 "frame": self.frame,
                 "sprite": "morty_normal" #NOTE: Se envia el sprite de morty_normal porque Morty solo se moverá en el eje x cuando este curado
                 })

    @property #y es una property ya que necesitamos que esta no exeda los limites de la pantalla (display) y donde se envia la señal al frontend (MainWindow)
    def y(self):
        return self.__y

    @y.setter #Con el setter verificamos que y tome valores entre -35 y self.display_y + 5 (no icluidos) y verificamos si llego al final de la pantalla (verticalmente)
    def y(self, value):
        if -35 < value < self.display_y + 5:
            self.__y = value
            self.update_position_signal.emit( #Emitimos una señal hacia el MainWindow para que se updatee el frontend de Morty (QLabel y QPixmap)
                {'char': self._id,
                 'x': self.x,
                 'y': self.y,
                 "frame": self.frame,
                 "sprite": "morty"
                 })
        else:
            self.update_position_signal.emit(
                {'char': self._id,
                'delete': True})
            self.alive = False #En caso de que haya llegado al final (vertical), lo destruimos
    
    def run(self):
        time.sleep(self.waiting) #Esperamos el "tiempo de espera" de cada cuanto aparece un Morty
        while self.alive:
            time.sleep(0.1) #Se determina el "tick" (cada cuanto se actualiza) de Morty
            self.frame += 1 #Se actualiza el frame de Morty
            self.y += 5 + self.speed #Se actualiza la posicion (backend) de Morty
        if self.cured: #Revisamos si se ha curado
            self.update_position_signal.emit( #Emitimos una señal hacia el MainWindow para que se actualize el frontend de Morty (QLabel y QPixmap) y lo cambie a un Morty curado   
                    {'char': self._id,
                     'x': self.x,
                     'y': self.y,
                     "frame": 0,
                     "sprite": "morty_cured"
                     })
            self.frame = 1 #Seteamos el frame a 1 para que Morty mire a la izquierda
            time.sleep(2)
            while self.x > -35: #Hacemos un ciclo para que Morty camine hacia la izquierda
                self.x -= 5
                self.frame += 1
                time.sleep(0.1)

    def shooted(self): #Metodo que determina que pasa cuando Morty recive una jeringa
        self.alive = False
        self.cured = True


class RickSanchez(core.QObject): #Importamos QObject 
                                    #The More You Know: (QObject es el objeto base de Qt, ejemplo de herencia:
                                    # QLabel hereda de -> QFrame hereda de -> QWidget hereda de -> QObject)
    update_position_signal = core.pyqtSignal(dict) #Señal que se comunica con el MainWindow para actualizar el frontend de RickSanchez y Syringer
    create_syringer_signal = core.pyqtSignal(dict) #Señal que se comunica con el MainWindow para crear (spawnear) una jeringa
    check_shoot_signal = core.pyqtSignal(dict) #Señal que se comunica con la A.I. para checkear el impacto de la jeringa con un Morty

    def __init__(self, x, y):   #Creamos los atributos:
                                    #x, y: determinan las dimensiones de la pantalla
        super().__init__()
        self.display_x = x
        self.display_y = y
        self.__x = x//2 #Determinamos la posicion x incial
        self.__y = y - 34 #Determinamos la posicion y incial
        self.points = 0
        self.syringers = dict() #Determinamos un almacenador de las jeringas que han sido disparadas
        self.__frame = 0 #Determinamos el frame inicial

    #Las properties son practicamente lo mismo que para Morty
    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, value):
        if 2 < value:
            self.__frame = 0
        else:
            self.__frame = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if 16 < value < self.display_x - 48:
            self.__x = value
            self.update_position_signal.emit(
                {'char': 'doc',
                 'x': self.x,
                 'y': self.y,
                 "frame": self.frame,
                 "sprite": "rick"
                 })

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if 0 < value < (self.display_y)-16-7:
            self.__y = value
            self.update_position_signal.emit(
                {'char': 'doc',
                 'x': self.x,
                 'y': self.y,
                 "frame": self.frame,
                 "sprite": "rick"
                 })

    def move(self, event): #Metodo que recive la señal del frontend (input del usuario). Aqui se actualiza el backend de RickSanchez
        self.frame += 1
        if event == 'R':
            self.x += 10
        if event == 'L':
            self.x -= 10

    def shoot(self): #Metodo que describe el disparo de un jeringa
        s_id = f"s_{len(self.syringers)}"   #Se genera un id para la jeringa
        s = Syringer(                       #Se instancia la jeringa
            self.x, self.y, s_id,
            self.update_position_signal,
            self.check_shoot_signal)
        self.create_syringer_signal.emit({"char": s_id, "x": self.x, "y": self.y}) #Se emite la señal para crear el frontend de la jeringa (Qlabel y Qpixmap)
        self.syringers[s_id] = s #Agregamos la jeringa al almacenador
        s.start() #Partimos el ciclo de la jeringa
    
    def impact_syringer(self, s_id): #Metodo que maneja el impacto de la jeringa
        self.syringers[s_id].impact() #Se ejecuta el metodo de impacto de la jeringa


class Syringer(core.QThread): #Importamos QThread 
    def __init__(self, x, y, _id, update_position_signal, check_shoot_signal): #Creamos loa atributos:
                                                                                    #x, y: determinan las dimensiones de la pantalla
                                                                                    #_id: para tener una referencia a cada Morty
                                                                                    #update_position_signal: para almacenar la señal que le paso RickSanchez   
                                                                                    #check_shoot_signal: para almacenar la señal que le paso RickSanchez   
        super().__init__()
        self.x = x
        self.__y = y
        self._id = _id
        self.update_position_signal = update_position_signal
        self.check_shoot_signal = check_shoot_signal
        self.alive = True #Booleano que determina si la jeringa esta "viva"
        

    @property #property parecida a la de Morty
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if -30 < value: #chequeamos que la jeringa este dentro del display
            self.__y = value
            self.update_position_signal.emit( #emitimos su posicion para que se actualize en el frontend (MainWindow)
                {'char': self._id, 'x': self.x, 'y': self.y})
            if value > 0:
                self.check_shoot_signal.emit( #chequeamos si ha impactado a algun Morty
                    {'x': self.x, 'y': self.y, 'a_id': self._id})
        else: #en el caso en que ya no este en el display, la eliminamos
            self.alive = False
    
    def run(self):
        while self.alive:
            time.sleep(0.07) #determinamos el tiempo de refresco del ciclo (frame rate)
            self.y -= 8 #movemos la jeringa
    
    def impact(self): #metodo que se encarga de la logica del impacto de la jeringa
        self.alive = False #se que "ya no esta viva"
        self.update_position_signal.emit( #se emite la informacion al forntend (MainWindow) para que se actualice su frontend
                {'char': self._id, 'delete': True})


class AI(core.QThread): #Importamos QThread

    start_signal = core.pyqtSignal(dict)
    arrow_impacted_signal = core.pyqtSignal(str) #señal que se conecta con RickSanchez para indicar el impacto de una jeringa
    create_morty_signal = core.pyqtSignal(dict) #señal que se conecta con el frontend (MainWindow) para crear el forntend de un Morty
    update_position_signal = core.pyqtSignal(dict) #señal que se conecta con el frontend (MainWindow) para actualizar el forntend de un Morty
    end_game_signal = core.pyqtSignal() #señal que se conecta con el frontend (MainWindow) para cerrar el juego en caso que se acabe el juego

    def __init__(self, x, y): #Creamos loa atributos:
                                #x, y: determinan las dimensiones de la pantalla
        super().__init__()

        self.display_x = x
        self.display_y = y

        self.mortys = [] #lista donde almacenamos todos los Mortys que haya

    def begin(self, data): #metodo que recive la sañal de partida del main
        if data: #chequeamos si data es True
            self.start() #partimos el QThread

    def run(self):
        win = True #variable con la que chequeamos si el jugador gano (parte como True debido a la forma en que esta implementada el juego)
        for r in range(3): #se establece el numero de rondas
            print("="*50) #informacion que se muestra en la consola
            print("RONDA:", r+1) #informacion que se muestra en la consola

            time.sleep(2) #establecemos un tiempo entre rondas
            print("\nComienza en:") #informacion que se muestra en la consola
            for t in range(3): #cuenta regresiva para que comienze la ronda
                print(3-t) #informacion que se muestra en la consola
                time.sleep(1) #frame rate del conteo
            print("¡Comenzó!\n") #informacion que se muestra en la consola
            mortys_in = 0 #contador de la cantidad de Mortys que han llegado al final de la pantalla
            wainting_time = 0 #contador del tiempo en que aparecen los Mortys
            for i in range(10 + 5*r): #determinamos cuantos Mortys creamos
                v_id = str(i) #id_ de Morty
                wainting_time += random.randint(2, 8) #agregamos un numero aleatorio al tiempo en que aparecen los Mortys
                self.create(v_id, 2*r, wainting_time) #creamos a un Morty
            while len(self.mortys) > 0: #aqui ocurre la logica de la ronda
                for m in self.mortys: #chequeamos a cada Morty
                    if mortys_in == 3: #chequeamos la condicion de termino de juego al inicio del for
                        break #salimos del for, ya que el jugador perdio
                    if m.isFinished(): #chequeamos si el Thread ha terminado
                        if not m.cured: #chequeamos si no ha sido curado
                            mortys_in += 1 #se agrega 1 al contador de Mortys que han llegado al final de la pantalla
                            print("¡Un Morty contagiado ha entrado!") #informacion que se muestra en la consola
                        self.mortys.remove(m) #eliminamos el Morty de la lista de Mortys
                if mortys_in == 3: #chequeamos la condicion de termino de nuevo (para cumplir todos los casos)
                    break #salimos del while, ya que el jugador ha perdido
            if mortys_in == 3: #chequeamos por ultima vez la conidcion de termino (ya que aqui se acabo el ciclo)
                win = False #determinamos que el jugador perdio
                break #salimos del for que determina las rondas
            print("\n¡RONDA SUPERADA!\n") #informacion que se muestra en la consola (ocurre si el jugador no ha perdido)
        if win: #chequeamos si el jugador ha ganado
            print("Felcidades, has ganado!!") #informacion que se muestra en la consola
        else:
            print("Oh no!, has perdido :(") #informacion que se muestra en la consola
        self.end_game_signal.emit() #emitimos la señal para que se cierre la MainWindow
        
    def create(self, v_id, speed, waiting): #metodo encargado de crear un Morty
        m = Morty(self.display_x, self.display_y, v_id, speed, waiting) #creamos el Morty
        m.update_position_signal = self.update_position_signal #le pasamos la señal para que el Morty la maneje
        self.mortys.append(m) #agregamos al Morty a la lista de Mortys
        data = {"char": v_id, "x": m.x, "y": m.y} #creamos la informacion de la creacion del Morty que sera emitida
        self.create_morty_signal.emit(data) #emitimos la informacion al forntend (MainWindow)
        m.start() #iniciamos el QThread
    
    def check_shoot(self, data): #metodo que recive la informacion de la señal check_shoot_signal de Syringer
        x = data["x"] #alamcenamos la posicion x
        y = data["y"] #almacenamos la posicion y
        for m in self.mortys: #accedemos a cada Morty en la lista de Mortys
            if not m.alive: #chequeamos si no esta vivo
                continue #pasamos al siguiente Morty
            v_x = m.x #almacenamos la posicion x de Morty
            v_y = m.y #almacenamos la posicion y de Morty
            d_x = x - v_x #almacenamos la distancia entre la posicion x de la jeringa y la posicion x de Morty
            if not (-10 < d_x < 26): #chequeamos si la jeringa no impacto (si la difencia de distancias no esta en ese rango)
                continue #pasamos al siguiente Morty
            d_y = y - v_y #almacenamos la distancia entre la posicion y de la jeringa y la posicion y de Morty
            if d_y > 30: #chequeamos si la jeringa no impacto
                continue #pasamos al siguiente Morty
            #en caso de que ambos impactos sean True
            m.shooted() #ejecutamos el metodo que determina que ocurre si Morty recive una jeringa
            self.arrow_impacted_signal.emit(data["a_id"]) #emitimos la informacion de la jeringa al forntend (MainWindow) para eliminar la jeringa


