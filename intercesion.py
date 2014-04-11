import threading
import semaforo
import pygame

class intercession(pygame.sprite.Sprite):
  """docstring for intercession"""
  def __init__(self, x,y,rails):
    super(intercession, self).__init__()

    self.rect=pygame.Rect(x,y,50,102)
    eventoX = threading.Event()
    eventoY = threading.Event()
    self.semaforo = semaforo.Semaforo(eventoX, eventoY)
    self.semaforo.iniciar()
