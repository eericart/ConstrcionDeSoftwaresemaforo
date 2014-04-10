import threading
from direccion import Directions
from llist import dllist, dllistnode


class Car(threading.Thread):
  """docstring for Vehiculo"""
  def __init__(self,posicionX,posicionY,direction, interInicial):
    super(Car, self).__init__()
    self.direction = direction
    self.posicionX = posicionX
    self.posicionY = posicionY
    self.currentIntercesion = interInicial
    print self.name

  def accelerate (self,calle,speed=1):

    if self.revisarSemaforo(calle) == "verde":
      if self.direction == Directions().north:
        self.posicionY -= 10+speed
        if self.posicionY < 1:
          self.posicionY =640

      elif self.direction == Directions().south:
        self.posicionY += 10+speed
        if self.posicionY > 640:
          self.posicionY = 0

      elif self.direction == Directions().east:
        self.posicionX += 10+speed
        if self.posicionX > 1024:
          self.posicionX =0

      else :
        self.posicionX -=  10+ speed
        if self.posicionX < 1:
          self.posicionX = 1024

  def revisarSemaforo(self, calle):
    self.nextInter(calle)
    if self.direction == Directions().east or self.direction == Directions().west:
      return self.currentIntercesion.semaforo.estadoX
    else:
      return self.currentIntercesion.semaforo.estadoY

  def nextInter (self,calle):
    intercesiones = dllist(calle.intercessiones)
    inter = intercesiones.first
    while True:
      try :
        if inter.value == self.currentIntercesion:
          if self.direction == Directions().east or self.direction == Directions().north:
            try:
              self.currentIntercesion = inter.prev.value
            except AttributeError:
              self.currentIntercesion = intercesiones.last.value
            break
          else:
            try:
              self.currentIntercesion = inter.next.value
            except AttributeError:
              self.currentIntercesion = intercesiones.first.value
            break
      except:
        break
      inter = inter.next


  def reduce (self,calle):
    self.accelerate(calle, -9)
    pass

