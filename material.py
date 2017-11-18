
from color import Color


# about built-in material:
# basic attrs:
# >color
# >illumination:[0..1]
# >reflect:[0..1]
# >refract:[0..1]
class Material(object):
	def __init__(self,color=Color.black(),illu=0,reflect=0,refract=0):
		self.color=color
		self.illu=illu
		self.reflect=reflect
		self.refract=refract