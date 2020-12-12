import threading
import time
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# Lista de tramos
tramos = [1, 2]

tramoOcupado = False
cantidadDeTrenes = 4

# Lleva la cuenta de cuantos trenes hay esperando en cada tramo
esperandoTramo1 = 0
esperandoTramo2 = 0

#Recuerda en cual tramo entro la ultima vez
ultimaEntrada = 1


class Tren(threading.Thread):
    def __init__(self, monitor, tramo , numeroTren):
        super().__init__()
        self.monitor = monitor
        self.tramo = tramo
        self.nombre = 'Tren' + str(numeroTren)
  
    def entraTren(self,tramo):
        global esperandoTramo1, esperandoTramo2, tramoOcupado, ultimaEntrada, trenes, tramos
        with self.monitor:
            if (self.tramo == tramos[0]):
                trenes.append(1)
                esperandoTramo1 += 1 
                while(tramoOcupado or ultimaEntrada == 1 and esperandoTramo2 > 0 ):
                    self.monitor.wait()
                esperandoTramo1 -= 1
                tramoOcupado = True
                ultimaEntrada = 1
                

            if (self.tramo == tramos[1]):
                esperandoTramo2 += 1
                trenes.append(0)
                while(tramoOcupado or ultimaEntrada == 2 and esperandoTramo1 > 0):
                    self.monitor.wait()
                esperandoTramo2 -= 1
                tramoOcupado = True
                ultimaEntrada = 2
               
        logging.info(f'Entra  ' +str(self.nombre) + ' en el tramo '+ str(self.tramo))
        time.sleep(2)

    def saleTren(self):
        global tramoOcupado, trenes
        with self.monitor:
            trenes.pop(0)
            tramoOcupado = False
            self.monitor.notify()
           
        logging.info(f'Sale ' +str(self.nombre) + ' en el tramo '+ str(self.tramo))
        time.sleep(2)
    
    def run(self):
        logging.info(f'Esta llegando el  ' + str(self.nombre))
        if (len(trenes) == 0):
            self.entraTren(self.tramo)
        else:
            self.saleTren()
        

# lista de trenes
trenes = []

# El monitor
tramos_monit = threading.Condition()


# arrancan los trenes
for i in range(cantidadDeTrenes):
    tipoDeTramos = random.randint(1,2)
    A = Tren(tramos_monit,tipoDeTramos,i)
    A.start()



    




  

