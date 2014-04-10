import threading
import semaforo
import pygame

class intercession(pygame.sprite.Sprite):
  """docstring for intercession"""
  def __init__(self, x,y,rails):
    super(intercession, self).__init__()
<<<<<<< HEAD
    self.x = x
    self.y = y
    eventoX = threading.event()
    eventoY = threading.event()
    self.semaforo = semaforo(eventoX, eventoY)
=======
    self.image = pygame.image.load("Images/asphalt-3-"+str(rails)+".png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    eventoX = threading.Event()
    eventoY = threading.Event()
    self.semaforo = semaforo.Semaforo(eventoX, eventoY)
>>>>>>> 9537a8f7c1def7793aa341c5131a7d9744a16fda
    self.semaforo.iniciar()

