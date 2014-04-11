#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
import calle
import vehiculo
import direccion
import intercesion


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
        for inter in street.intercessiones:
            pygame.draw.rect(self.screen, Color(inter.semaforo.estadoX),inter.rect,2)
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador Semaforo")

    street = calle.Street(0,320,4,direccion.Directions().east)
    inter= intercesion.intercession (135,348,4)
    street.intercessiones.append(inter)
    car = vehiculo.Car(1000,380,direccion.Directions().east,street.intercessiones[0])
    street.cars.append(car)
    simulator = Simulator(screen)
    simulator.streets.append(street)

    car2 = vehiculo.Car(525,380,direccion.Directions().north,street.intercessiones[0])
    street2 = calle.Street(550,0,2,direccion.Directions().north)
    street2.cars.append(car2)
    inter2= intercesion.intercession (512,348,4)
    street2.intercessiones.append(inter2)
    street.intercessiones.append(inter2)
    simulator.streets.append(street2)

    street3 = calle.Street(800, 0, 2, direccion.Directions().north)
    simulator.streets.append(street3)
    inter3 = intercesion.intercession(780, 348, 4)
    street3.intercessiones.append(inter3)
    street.intercessiones.append(inter3)
    car3 = vehiculo.Car(795, 380, direccion.Directions().south, street.intercessiones[0])
    street3.cars.append(car3)

    dirt= pygame.Rect(0, 100, 10, 10)

    for street in simulator.streets:
        for car in street.cars:
            car.start()


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