import threading

class intercession(object):
  """docstring for intercession"""
  def __init__(self, x,y):
    super(intercession, self).__init__()
    self.x = x
    self.y = y
    eventoX = threading.event()
    eventoY = threading.event()
    self.semaforo = semaforo(eventoX, eventoY)

<<<<<<< HEAD
  def crearInterseccion(): 
  	
     self.semaforo.iniciar()
=======
    #Evento X y Y que representa el semaforo de cada calle.
>>>>>>> fe37b483f447c25e780669bca3141721417c0848
