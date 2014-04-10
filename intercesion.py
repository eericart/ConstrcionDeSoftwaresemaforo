import threading
import semaforo
class intercession(object):
  """docstring for intercession"""
  def __init__(self, x,y):
    super(intercession, self).__init__()
    self.x = x
    self.y = y
    eventoX = threading.Event()
    eventoY = threading.Event()
    self.semaforo = semaforo.Semaforo(eventoX, eventoY)
    self.semaforo.iniciar()

