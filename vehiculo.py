import threading
from direccion import Directions

class Car(threading.Thread):
  """docstring for Vehiculo"""
  def __init__(self,posicionX,posicionY,direction):
    super(Car, self).__init__()
    self.direction = direction
    self.posicionX = posicionX
    self.posicionY = posicionY
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

  def brake ():
    pass
  def reduce ():
    pass
