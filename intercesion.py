import threading
import semaforo
class intercession(object):
  """docstring for intercession"""
  def __init__(self, x,y):
    super(intercession, self).__init__()
    self.x = x
    self.y = y
<<<<<<< HEAD
    eventoX = threading.event()
    eventoY = threading.event()
    self.semaforo = semaforo(eventoX, eventoY)
    self.semaforo.iniciar()
=======
    eventoX = threading.Event()
    eventoY = threading.Event()
    self.semaforo = semaforo.Semaforo(eventoX, eventoY)
    self.semaforo.iniciar()

>>>>>>> ff2755d0c13bd5c36d9aebb0ec04c39ad82ec14a
