import time
import threading
from random import randint

class Semaforo():
  """docstring for ClassName"""
  def __init__(self, eventX, eventY):
    self.estadoX = "green"
    self.estadoY = "red"
    self.eventoX = eventX
    self.eventoY = eventY
    self.eventoX.set()

  def cambio(self):
    if self.estadoX == "green":
      self.estadoX = "yellow"
    elif self.estadoX == "yellow":
      self.estadoX = "red"
      self.estadoY = "green"
      self.eventoX.clear()
      self.eventoY.set()
    elif self.estadoY == "green":
      self.estadoY = "yellow"
    elif self.estadoY == "yellow":
      self.estadoY = "red"
      self.estadoX = "green"
      self.eventoX.set()
      self.eventoY.clear()
    print self.estadoX

  def iniciar(self):
    if self.estadoX == "green" or self.estadoY == "green":
  	  threading.Timer(2, self.iniciar).start()
    else:
      threading.Timer(7, self.iniciar).start()
    self.cambio()
