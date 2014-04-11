import threading
from direccion import Directions
import pygame
import itertools



class Car(threading.Thread, pygame.sprite.Sprite):
  """docstring for Vehiculo"""
  def __init__(self,posicionX,posicionY,direction, interInicial):
    super(Car, self).__init__()
    self.direction = direction
    self.currentIntercesion = interInicial
    self.car_path = "Images/car-"
    self.image= pygame.image.load(self.car_path+str(self.direction)+".png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.centerx  = posicionX
    self.rect.centery = posicionY
    self.estado = "verde"
    print self.name

  def accelerate (self,calle,speed=1):
    if self.estado == "verde":
      if self.direction == Directions().north:
        self.rect.centery -= 1+speed
        if self.rect.centery < 1:
          self.rect.centery =640

      elif self.direction == Directions().south:
        self.rect.centery += 1+speed
        if self.rect.centery > 640:
          self.rect.centery = 0

      elif self.direction == Directions().east:
        self.rect.centerx += 1+speed
        if self.rect.centerx > 1024:
          self.rect.centerx =0

      else :
        self.rect.centerx -=  10+ speed
        if self.rect.centerx < 1:
          self.rect.centerx = 1024

    for inter,car in itertools.izip_longest(calle.intercessiones, calle.cars):
      try:
        if pygame.sprite.collide_rect(self, inter):
          if self.direction == Directions().east or self.direction == Directions().west:
            self.estado = inter.semaforo.estadoX
          else:
            self.estado = inter.semaforo.estadoY

        if pygame.sprite.collide_rect(self, car) and self != car:
          if self.direction == Directions().east or self.direction == Directions().west:
            self.estado = inter.semaforo.estadoX
          else:
            self.estado = inter.semaforo.estadoY
      except AttributeError:
        continue




