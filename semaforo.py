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

  def iniciar(self):
  	threading.Timer(15.0, self.iniciar).start()
  	self.cambio()
