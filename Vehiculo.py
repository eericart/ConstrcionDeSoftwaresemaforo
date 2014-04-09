import threading

class Car(threading.Thread):
  """docstring for Vehiculo"""
  def __init__(self,posicionInicion,directions):
    super(Vehiculo, self).__init__()
    self.posicionInicion = posicionInicion
    self.directions = directions
    print self.name
