import intercesion

class Street(object):
  """docstring for Street"""
  def __init__(self, x,y,directions):
    super(Street, self).__init__()
    self.x = x
    self.y = y
    self.intercessiones = []
    self.directions = directions
    self.cars = []
    #self.check = []