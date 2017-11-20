from color import Color
import multiprocessing

__author__ = 'tabokie'

class Canvas(object):
	def __init__(self,w,h,p):
		self.width=w
		self.height=h
		self.pixels=p
	def clear(self):
		self.pixels.fill(0)
	def put_pixel(self,x,y,color):
		index=int(y)*self.width+int(x)
		try:
			self.pixels[index]=Color.uint32(color)
		except IndexError:
			print(x,y)

	def draw_scene(self,scene):
		for x in range(self.width):
			for y in range(self.height):
				self.put_pixel(x,y,scene.sample(x,y))
		# self.dispatch_draw(scene)

	def draw_single_thread(self,scene,x,y,w,h):
		# print(">>>>>>>>>",x,y,'->',)
		for dx in range(w):
			for dy in range(h):
				self.put_pixel(x+dx,y+dy,scene.sample(x+dx,y+dy))

	def dispatch_draw(self,scene):
		# 4-thread
		a=multiprocessing.Process(target=self.draw_single_thread,args=(scene,0,0,self.width//2,self.height//2))
		b=multiprocessing.Process(target=self.draw_single_thread,args=(scene,self.width//2,0,self.width-self.width//2,self.height//2))
		c=multiprocessing.Process(target=self.draw_single_thread,args=(scene,0,self.height//2,self.width//2,self.height-self.height//2))
		d=multiprocessing.Process(target=self.draw_single_thread,args=(scene,self.width//2,self.height//2,self.width-self.width//2,self.height-self.height//2))
		a.start()
		b.start()
		c.start()
		d.start()

