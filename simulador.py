#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
import calle
import vehiculo
import direccion
import intercesion
import itertools


WIDTH = 1024
HEIGHT = 640

class Simulator(object):
  """docstring for Simulator"""
  def __init__(self, screen):
    super(Simulator, self).__init__()
    self.streets = []
    self.screen = screen
    self.asphalt_sprite = pygame.image.load("Images/asphalt-1.png").convert_alpha()
    self.background_image = pygame.image.load("Images/background2.png").convert()



  def draw (self):
    self.screen.blit(self.background_image, (0, 0))
    for street in self.streets:
        for car in street.cars:
            self.screen.blit(car.image,(car.rect))
            car.accelerate(street)
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador Semaforo")

    street = calle.Street(0,320,4,direccion.Directions().east)
    inter= intercesion.intercession (340,220,4)
    street.intercessiones.append(inter)
    car = vehiculo.Car(1000,220,direccion.Directions().east,street.intercessiones[0])
    street.cars.append(car)
    simulator = Simulator(screen)
    simulator.streets.append(street)
    street2 = calle.Street(550,0,2,direccion.Directions().north)
    inter= intercesion.intercession (340,220,4)
    street.intercessiones.append(inter)
    simulator.streets.append(street2)
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