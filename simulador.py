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
  def __init__(self):
    super(Simulator, self).__init__()
    self.streets = []
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.asphalt_sprite = pygame.image.load("Images/asphalt-1.png").convert_alpha()
    self.background_image = pygame.image.load("Images/background.png").convert()
    self.car_path = "Images/car-"


  def draw (self):
    self.screen.blit(self.background_image, (0, 0))


    for street in self.streets:
        for rail in xrange(0,street.rails):
            for x in xrange(street.x,WIDTH,32):
                self.screen.blit(self.asphalt_sprite,(x,220+32*rail))
        for car in street.cars:
            c= pygame.image.load(self.car_path+str(car.direction)+".png").convert_alpha()
            print "mueve"
            self.screen.blit(c,(car.posicionX,car.posicionY))
    pygame.display.flip()

def main():
    pygame.display.set_caption("Simulador Semaforo")

    street = calle.Street(0,320,4,direccion.Directions().east)
    inter= intercesion.intercession (4,220)
    street.intercessiones.append(inter)
    car = vehiculo.Car(1000,220,direccion.Directions().east,street.intercessiones[0].x)
    street.cars.append(car)
    simulator = Simulator()
    simulator.streets.append (street)

    for street in simulator.streets:
        for car in street.cars:
            car.start()
            car.run(street)


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