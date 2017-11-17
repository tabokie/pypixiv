import math
from color import Color
from random import random as rand

class Obj(object):
	def __init__(self,code,args):
		self.handlers={
			0 : self.initCircle
		}
		init=self.handlers.get(code,self.init404)
		init(args)
	def initCircle(self,args):
		# args:[x,y,r,a]
		self.sdf=(lambda x,y: ( ((x-args[0])**2+(y-args[1])**2)**0.5-args[2] , args[3] ) )
	def init404(self,args):
		self.sdf=None
		pass
	def __add__(self,other):
		new=Obj.Nil()
		new.sdf=(lambda x,y: self.sdf(x,y) if self.sdf(x,y)[0]<other.sdf(x,y)[0] else other.sdf(x,y))
		return new
	def __sub__(self,other):
		new=Obj.Nil()
		new.sdf=(lambda x,y: self.sdf(x,y) if self.sdf(x,y)[0]+other.sdf(x,y)[0]>=0 else (-other.sdf(x,y)[0],self.sdf(x,y)[1]))
		return new
	def __mul__(self,other):
		new=Obj.Nil()
		new.sdf=(lambda x,y: self.sdf(x,y) if self.sdf(x,y)[0]>other.sdf(x,y)[0] else other.sdf(x,y))
		return new

	@staticmethod
	def Nil():
		return Obj(-1,[])
