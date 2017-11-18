
from color import Color


# about built-in material:
# basic attrs:
# >color
# >illumination:[0..1]
# >reflect:[0..1]
# >refract:[0..1]
class Material(object):
	def __init__(self,c=Color.black(),i=0,reflect=0,refract=0):
		self.color=c
		self.illumination=i
		self.reflect=reflect
		self.refract=refract