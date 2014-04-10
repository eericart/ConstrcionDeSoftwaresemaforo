import time
import threading

class Semaforo():
  """docstring for ClassName"""
  def __init__(self, eventX, eventY):
    self.estadoX = "verde"
    self.estadoY = "rojo"
    self.eventoX = eventX
    self.eventoY = eventY
    self.eventoX.set()
    
  def cambio(self):
    if self.estadoX == "verde":
      self.estadoX = "amarillo"
    elif self.estadoX == "amarillo":
      self.estadoX = "rojo"
      self.estadoY = "verde"
      self.eventoX.clear()
      self.eventoY.set()
    elif self.estadoY == "verde":
      self.estadoY = "amarillo"
    elif self.estadoY == "amarillo":
      self.estadoY = "rojo"
      self.estadoX = "verde"
      self.eventoX.set()
      self.eventoY.clear()
    print  "estadoY " + self.estadoY + "  >> estadoX " + self.estadoX
    print "EventoY " +  str(self.eventoY.is_set()) +"  >> EventoX " +str(self.eventoX.is_set())

  def iniciar(self):
  	self.cambio()
  	threading.Timer(15.0, self.iniciar).start()

eventoX = threading.Event()
eventoY = threading.Event()
x = Semaforo(eventoX, eventoY)
x.iniciar()