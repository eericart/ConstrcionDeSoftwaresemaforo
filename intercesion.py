import threading 

class intercession(object):
  """docstring for intercession"""
  def __init__(self, x,y, semaforo):
    super(intercession, self).__init__()
    self.x = x
    self.y = y
    self.semaforo = semaforo

    #Evento X y Y que representa el semaforo de cada calle. 

  eventoX = threading.event()
  eventoY = threading.event()

  self.intercession = semaforo(eventoX, eventoY)
  x.iniciar()