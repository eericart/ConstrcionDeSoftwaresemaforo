import threading
from direccion import Directions
import pygame
import itertools



class Car(threading.Thread, pygame.sprite.Sprite):
  """docstring for Vehiculo"""
  def __init__(self,posicionX,posicionY,direction):
    super(Car, self).__init__()
    self.direction = direction
    self.car_path = "Images/car-"
    self.image= pygame.image.load(self.car_path+str(self.direction)+".png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.centerx  = posicionX
    self.rect.centery = posicionY
    self.estado = "green"
    print self.name

  def accelerate (self,calle,speed=1):

    if self.estado == "green":
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
        self.rect.centerx -=  1+ speed
        if self.rect.centerx < 1:
          self.rect.centerx = 1024

    elif self.estado == "yellow":
      if self.direction == Directions().north:
        self.rect.centery -= speed
        if self.rect.centery < 1:
          self.rect.centery = 640

      elif self.direction == Directions().south:
        self.rect.centery += speed
        if self.rect.centery > 640:
          self.rect.centery = 0

      elif self.direction == Directions().east:
        self.rect.centerx += speed
        if self.rect.centerx > 1024:
          self.rect.centerx =0

      else :
        self.rect.centerx -=  speed
        if self.rect.centerx < 1:
          self.rect.centerx = 1024


    for check in calle.check:
      if pygame.sprite.collide_rect(self, check):

        if self.direction == Directions().east or self.direction == Directions().west: 
          if check.semaforo.estadoX == "yellow" or check.semaforo.estadoX == "red":
            self.estado = "yellow"
        else:
          if check.semaforo.estadoY == "yellow" or check.semaforo.estadoY == "red":
            self.estado = "yellow"
   
    for inter,car in itertools.izip_longest(calle.intercessiones, calle.cars):
      try:
        if pygame.sprite.collide_rect(self, inter):
          if self.direction == Directions().east or self.direction == Directions().west:
            if inter.semaforo.estadoX == "green" or inter.semaforo.estadoX == "red":

              self.estado = inter.semaforo.estadoX

              if self.direction == Directions().east and self.self.rect.center > inter.x:
                self.estado = "green"

            else: 
              self.estado = "green"

          else:
            if inter.semaforo.estadoY == "green" or inter.semaforo.estadoY == "red":
              self.estado = inter.semaforo.estadoY
            else:
              self.estado = "green"

        if pygame.sprite.collide_rect(self, car) and self != car:
          if self.direction == Directions().east or self.direction == Directions().west:
            self.estado = inter.semaforo.estadoX
          else:
            self.estado = inter.semaforo.estadoY
      except AttributeError:
        continue




