import math
from color import Color
from random import random as rand

__author__ = 'tabokie'

class Sdf(object):
	def __init__(self):
		self.sdf=None
	def __add__(self,other):
		new=Sdf()
		new.sdf=(lambda x,y: self.sdf(x,y) if self.sdf(x,y)[0]<other.sdf(x,y)[0] else other.sdf(x,y))
		return new
	def __sub__(self,other):
		new=Sdf()
		new.sdf=(lambda x,y: self.sdf(x,y) if self.sdf(x,y)[0]+other.sdf(x,y)[0]>=0 else (-other.sdf(x,y)[0],self.sdf(x,y)[1]))
		return new
	def __mul__(self,other):
		new=Sdf()
		new.sdf=(lambda x,y: self.sdf(x,y) if self.sdf(x,y)[0]>other.sdf(x,y)[0] else other.sdf(x,y))
		return new
	@staticmethod
	def Circle(args):
		# args:[x,y,r,a]
		new = Sdf()
		new.sdf=(lambda x,y: ( ((x-args[0])**2+(y-args[1])**2)**0.5-args[2] , args[3] ) )
		return new
	@staticmethod
	def Plane(args):
		# args:[x0,y0,nx,ny,a]
		new = Sdf()
		norm=(args[2]**2+args[3]**2)**0.5
		new.sdf=(lambda x,y: ( abs((x-args[0])*args[2]/norm+(y-args[1])*args[3]/norm) , args[4] ))
		return new
	@staticmethod
	def DirectedPlane(args):
		# args:[x0,y0,nx,ny,a]
		new = Sdf()
		norm=(args[2]**2+args[3]**2)**0.5
		new.sdf=(lambda x,y: ( -((x-args[0])*args[2]/norm+(y-args[1])*args[3]/norm) , args[4] ))
		return new

class Obj(Sdf):
	def __init__(self,code,args):
		self.handlers={
			0 : self.initCircle,
			1 : self.initPlane,
			2 : self.initDirectedPlane,
			3 : self.initTriangle
		}
		init=self.handlers.get(code,self.init404)
		init(args)
	def initCircle(self,args):
		# args:[x,y,r,a]
		self.sdf=Sdf.Circle(args).sdf
	def initPlane(self,args):
		# args:[x0,y0,nx,ny,a]
		self.sdf=Sdf.Plane(args).sdf
	def initDirectedPlane(self,args):
		# args:[x0,y0,nx,ny,a]
		self.sdf=Sdf.DirectedPlane(args).sdf
	def initTriangle(self, args):
		# args:[x1,y1,x2,y2,x3,y3,a]
		(x1,y1)=args[0],args[1]
		(x2,y2)=args[2],args[3]
		(x3,y3)=args[4],args[5]
		color=args[6]
		# convert to 3 planes
		def _initArgs(x0,y0, x1,y1,x2,y2):
			args=[]
			A=(y2-y1)
			B=(x1-x2)
			C=(x2*y1-x1*y2)
			args.append((B**2*x0-A*B*y0-A*C)/(A**2+B**2))
			args.append((A**2*y0-A*B*x0-B*C)/(A**2+B**2))
			args.append(x0-args[0])
			args.append(y0-args[1])
			args.append(color)
			# print(args)
			return args
		self.sdf=(Sdf.DirectedPlane(_initArgs(x1,y1,x2,y2,x3,y3))*Sdf.DirectedPlane(_initArgs(x2,y2,x1,y1,x3,y3))*Sdf.DirectedPlane(_initArgs(x3,y3,x1,y1,x2,y2))).sdf
	def init404(self,args):
		self.sdf=None
		pass
	
