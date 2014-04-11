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
        #for check in street.check:
            #pygame.draw.rect(self.screen, Color(check.semaforo.estadoX), check.rect, 2)
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador Semaforo")

    #TEST

    #Intercesiones
    inter= intercesion.intercession (135,348,4, 50, 102)
    inter2= intercesion.intercession (512,348,4, 50, 102)
    inter3 = intercesion.intercession(780, 348, 4, 50, 102)

    #Calles
    streetPrinciparl = calle.Street(0,320,4,direccion.Directions().east)
    street = calle.Street(0,320,4,direccion.Directions().north)
    street2 = calle.Street(550,0,2,direccion.Directions().north)
    street3 = calle.Street(800, 0, 2, direccion.Directions().north)

    #Cars
    car = vehiculo.Car(1000,380,direccion.Directions().east)
    car4 = vehiculo.Car(150,200,direccion.Directions().north)
    car2 = vehiculo.Car(525,500,direccion.Directions().north)
    car3 = vehiculo.Car(795, 0, direccion.Directions().south)

    #Checks

    check11 = intercesion.intercession(85, 348, 4, 50, 102)
    check12 = intercesion.intercession(185, 348, 4, 50, 102)
    check21 = intercesion.intercession(462, 348, 4, 50, 102)
    check22 = intercesion.intercession(562, 348, 4, 50, 102)
    check31 = intercesion.intercession(730, 348, 4, 50, 102)
    check32 = intercesion.intercession(830, 348, 4, 50, 102)
    streetPrinciparl.check.extend([check11, check12, check21, check22, check31, check32])

    check1A = intercesion.intercession(135, 450, 4, 50, 50)
    street.check.append(check1A)
    check1B = intercesion.intercession(135, 298, 4, 50, 50)
    street.check.append(check1B)

    check2A = intercesion.intercession(512, 450, 4, 50, 50)
    street2.check.append(check2A)
    check2B = intercesion.intercession(512, 298, 4, 50, 50)
    street2.check.append(check2B)

    check3A = intercesion.intercession(780, 450, 4, 50, 50)
    street3.check.append(check3A)
    check3B = intercesion.intercession(780, 298, 4, 50, 50)
    street3.check.append(check3B)

    #Preparar
    streetPrinciparl.cars.append(car)
    street.cars.append(car4)
    street2.cars.append(car2)
    street3.cars.append(car3)

    streetPrinciparl.intercessiones.extend([inter3,inter,inter2])
    street.intercessiones.append(inter)
    street2.intercessiones.append(inter2)
    street3.intercessiones.append(inter3)

    simulator = Simulator(screen)
    simulator.streets.extend([streetPrinciparl,street,street2,street3])

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