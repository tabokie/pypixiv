#from vector import Vector
#from vertex import Vertex
#from color import Color
from random import random as rand
import math
from obj import Obj
from color import Color
import sys

__author__ = 'tabokie'

class Scene(object):
	def __init__(self, code):
		self.handle=code
		self.initHandlers={
			0 : self.scene_0
		}
		self.initHandlers.get(self.handle,self.reset)()
		self.default=Color.default()
	def sample(self,x,y):
		N=64
		sum=Color.zero()
		for i in range(N):
			# a=i*math.pi*2/N
			a=rand()*math.pi*2
			sum+=self.trace(x,y,math.cos(a),math.sin(a))
			print('Sampling:(',x,',',y,')',end='\r')
		#Color.printColor(sum/N)
		return sum/N
	def trace(self,x,y,dx,dy):
		t=0
		i=0
		MAX_STEP=60
		MAX_DIS=300
		Err=1
		while i<MAX_STEP and t<MAX_DIS:
			sd = self.objects.sdf(x+dx*t,y+dy*t)
			if sd[0]<Err:
				return sd[1]
			t+=sd[0]
		return self.default
	def reset(self):
		self.objects=Obj(-1)
	def scene_0(self):
		# self.objects=Obj(2,[200,200,0.5,0.5,Color.white()])
		self.objects=Obj(3,[50,80,180,140,100,300,Color.white()])
		# self.objects=Obj(0,[100,100,50,Color.white()])+Obj(0,[150,190,50,Color.black()])+Obj(1,[200,200,0.5,0.5,Color.white()])
	def scene404(self):
		self.reset()
		pass