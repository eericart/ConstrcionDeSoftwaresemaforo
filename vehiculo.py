import threading
from direccion import Directions

class Car(threading.Thread):
  """docstring for Vehiculo"""
  def __init__(self,posicionX,posicionY,direction, semaforo):
    super(Car, self).__init__()
    self.direction = direction
    self.posicionX = posicionX
    self.posicionY = posicionY
    self.nextIntercesion = semaforo
    print self.name

  def accelerate (self):
    if self.direction == Directions().north:
      self.posicionY -= 1
      if self.posicionY < 1:
          self.posicionY =640

    elif self.direction == Directions().south:
      self.posicionY += 1
      if self.posicionY > 640:
          self.posicionY = 0

    elif self.direction == Directions().east:
      self.posicionX += 1
      if self.posicionX > 1024:
           self.posicionX =0

    else :
      self.posicionX -=  1
      if self.posicionX < 1:
          self.posicionX = 1024

  def revisarSemaforo(self, calle):
    if len (calle.intercessiones) == 0: return "verde"
    estado=""
    for i in xrange(0,len(calle.intercessiones)):
      if self.direction == Directions().east or self.direction == Directions().west:
        if self.nextIntercesion == calle.intercessiones[i].x:
          estado=calle.intercessiones[i].semaforo.estadoX
          try :
            self.nextIntercesion =calle.intercessiones[i+1].x
          except :
            self.nextIntercesion = calle.intercessiones[0].x

        return estado

  def run(self,calle):
    while self.revisarSemaforo(calle) == "verde":
      self.accelerate()

  def reduce ():
    pass

