from enum import Enum
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cantidadDeTrenes = 3
tramoOcupado = False

# Lleva la cuenta de cuantos trenes hay esperando en cada tramo
esperandoTramo1 = 0
esperandoTramo2 = 0

#Recuerda en cual tramo entro la ultima vez
ultimaEntrada = 1

class Tramo(int,Enum):
    Tramo1 = 1
    Tramo2 = 2

class Tren(threading.Thread):
  def __init__(self,monitor, tramo = Tramo,numeroTren):
    super().__init__()
    self.monitor = monitor
    self.tramo = tramo
    self.nombre = f'Tren {numeroTren}'
  
    def entraTren(self,tramo):
        with self.monitor:
            if (self.tramo == 1 and len(trenes) == 0):
                esperandoTramo1 += 1 
                tren.append(0)
                while(tramoOcupado or ultimaEntrada == 1 and esperandoTramo2 > 0 ):
                    self.monitor.wait()
                esperandoTramo1 -= 1
                tramoOcupado = True
                ultimaEntrada = 1
            if(self.tramo == 2 and len(trenes) == 0):
                esperandoTramo2 += 1
                tren.append(0)
                while(tramoOcupado or ultimaEntrada == 2 and esperandoTramo1 > 0):
                    self.monitor.wait()
                esperandoTramo2 -= 1
                tramoOcupado = True
                ultimaEntrada = 2
        logging.info(f'Entra tren',str(self.tramo))
        time.sleep(1)

    def saleTren(self,tramo):
        with self.monitor:
            tren.pop(0)
            tramoOcupado = False
            self.monitor.notify()
        logging.info(f'Sale tren',str(self.tramo))
        time.sleep(1)
    
    def run(self):
        while(true):
            logging.info(f'Esta pasando el tren',str(self.nombre()))
            self.entraTren(self,tramo)
            self.saleTren(self,tramo)

# lista de trenes
trenes = []

# El monitor
trenes_monit = threading.Condition()

# arrancan los trenes
for tren in range(cantidadDeTrenes):
    A = Tren(trenes_monit,Tramo.Tramo1,tren)
    A.start()



    




  

