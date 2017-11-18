import operator

__author__ = 'tabokie'

class Color(object):
	def __init__(self,r,g,b,a):
		self.r=r
		self.g=g
		self.b=b
		self.a=a
	def _operation(self,other,op):
		r=op(self.r,other.r)
		g=op(self.g,other.g)
		b=op(self.b,other.b)
		a=op(self.a,other.a)
		return Color(r,g,b,a)
	def __add__(self,other):
		return self._operation(other,operator.add)
	def __truediv__(self,deno):
		#numericType=[int,float]
		return Color(self.r/deno,self.g/deno,self.b/deno,self.a/deno)
	@staticmethod
	def printColor(c):
		print('R:',int(c.r*255),' G:',int(c.g*255),' B:',int(c.b*255),' A:',int(c.a*255))
		return
	@staticmethod
	def uint32(c):
		return int(c.r*255)<<24|int(c.g*255)<<16|int(c.b*255)<<8|int(c.a*255)
	@staticmethod
	def white():
		return Color(1,1,1,1)
	@staticmethod
	def black():
		return Color(0,0,0,1)
	@staticmethod
	def zero():
		return Color(0,0,0,0)
	@staticmethod
	def default():
		return Color(0,0,0,1)

