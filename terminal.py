import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

tramoOcupado = False

# Lleva la cuenta de cuantos trenes hay esperando en cada tramo
esperandoTramo1 = 0
esperandoTramo2 = 0

#Recuerda en cual tramo entro la ultima vez
ultimaEntrada = 1


class Tramo(threading.Thread):
  def __init__(self,monitor):
    super().__init__()
    self.monitor = monitor
    self.tramo1 = tramo1
    self.tramo2 = tramo2
  
    def entraTren(self,tren):
        with self.monitor:
            if (self.tramo1 == 1):
                esperandoTramo1 += 1 
                while(tramoOcupado or ultimaEntrada == 1 and esperandoTramo2 > 0 ):
                    self.monitor.wait()
                esperandoTramo1 -= 1
                tramoOcupado = True
                ultimaEntrada = 1
            if(self.tramo2 == 2):
                esperandoTramo2 += 1
                while(tramoOcupado or ultimaEntrada == 2 and esperandoTramo1 > 0):
                    self.monitor.wait()
                esperandoTramo2 -= 1
                tramoOcupado = True
                ultimaEntrada = 2
        logging.info(f'Entra tren',str(self.nombre))
        time.sleep(1)

    def saleTren(self,tren):
        with self.monitor:
            tramoOcupado = False
            self.monitor.notify()
        logging.info(f'Sale tren',str(self.nombre))
        time.sleep(1)
    
    def run(self):
        while(true):
            self.entraTren(self,tren)
            self.saleTren(self,tren)

# lista de trenes
trenes = []
for tren in range(3):
    trenes.append(tren)

# El monitor
trenes_monit = threading.Condition()

# arrancan los trenes
for j in trenes:
    tramo = Tramo(trenes_monit)
    tramo.start()



    




  

