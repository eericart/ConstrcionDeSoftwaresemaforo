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
    self.semaforo.iniciar()