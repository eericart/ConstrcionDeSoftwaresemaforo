import intercesion
import threading
from pygame.locals import *
import vehiculo
import direccion
import intercesion


class Street(object):
  """docstring for Street"""
  def __init__(self, x,y,rails,directions):
	super(Street, self).__init__()
	self.x = x
	self.y = y
	self.rails = rails
	self.intercessiones = []
	self.directions = directions
	self.cars = []

  	def carGenerator(waitTime):
		car = []
		for x in range(10):
			car[x] = vehiculo.Car(1000,220,direccion.Directions().east,self.intercessiones[0])
			print 'Creado el ', car[x], 'carro'
			self.cars.append(car)

    #def carGenerator(tiempoEspera):
	
