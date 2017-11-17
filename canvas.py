from color import Color

class Canvas(object):
	def __init__(self,w,h,p):
		self.width=w
		self.height=h
		self.pixels=p
	def clear(self):
		self.pixels.fill(0)
	def put_pixel(self,x,y,color):
		index=int(y)*self.width+int(x)
		self.pixels[index]=Color.uint32(color)
	def draw_scene(self,scene):
		for x in range(self.width):
			for y in range(self.height):
				self.put_pixel(x,y,scene.sample(x,y))
