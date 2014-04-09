#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
import Calle
import Vehiculo

WIDTH = 1024
HEIGHT = 640

class Simulator(object):
  """docstring for Simulator"""
  def __init__(self):
    super(Simulator, self).__init__()
    self.streets = []
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.asphalt_sprite = pygame.image.load("Images/asphalt-1.png").convert_alpha()
    self.background_image = pygame.image.load("Images/background.png").convert()



  def draw (self):
    self.screen.blit(self.background_image, (0, 0))
    for street in self.streets:
      for rail in xrange(0,street.rails):
        for x in xrange(street.inicioX,WIDTH,32):
          self.screen.blit(self.asphalt_sprite,(x,220+32*rail))


def main():
    pygame.display.set_caption("Simulador Semaforo")

    street = Calle.Street(0,320,2)
    simulator = Simulator()
    simulator.streets.append (street)

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        simulator.draw()
        pygame.display.update()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()