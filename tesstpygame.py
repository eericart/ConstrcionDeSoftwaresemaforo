#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Importacion de los módulos
import pygame
from pygame.locals import *
import sys

# y cualquier otro modulo usado

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
# ----------------------------------------------
# Clases y Funciones utilizadas (lo explicare en la siguiente parte)
# ----------------------------------------------

def main():
    pygame.init()
    # La clase o función principal que crea o ejecuta el juego
    # Contiene principalmente loop del juego (el alma de este)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")
    fondo = pygame.image.load("Images/felt_grey.jpg").convert()
    tux = pygame.image.load("Images/car-l.png").convert_alpha()
    tux_pos_x = 1000
    tux_pos_y = 200

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

     # el bucle principal del juego
    while True:
        # le restamos 1 a la coordenada x de tux y comprobamos
        # que no alcance el borde de la pantalla
        tux_pos_x = tux_pos_x - 1
        if tux_pos_x < 1:
            tux_pos_x = 1000

        # Redibujamos todos los elementos de la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(tux, (tux_pos_x, tux_pos_y))
        # se muestran lo cambios en pantalla
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()