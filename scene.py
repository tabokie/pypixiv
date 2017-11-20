#from vector import Vector
#from vertex import Vertex
#from color import Color
from random import random as rand
import math
from obj import Obj
from color import Color
from material import Material
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
	# for pixel (x,y)
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
	# for ray(dx,dy) from (x,y)
	def trace(self,x,y,dx,dy,depth=1):
		t=0
		i=0
		MAX_STEP=10
		MAX_DIS=200
		Err=1
		while i<MAX_STEP and t<MAX_DIS:
			sd = self.objects.sdf(x+dx*t,y+dy*t)
			if sd[0]<Err:
				return self.second_trace(sd[1],x+dx*t,y+dx*t,dx,dy,depth)
			t+=sd[0] # why not = ?
		return self.default
	def second_trace(self,material,x,y,dx,dy,depth):
		if depth<=0:
			return material.color # seaching ends
		# sample=Color.zero()
		materialColor=material.color
		return material.illu*materialColor+material.reflect*(materialColor*self.trace_reflect(x,y,dx,dy,depth))# +material.refract*(materialColor*trace_refract(x,y,dx,dy,depth))
	def trace_reflect(self,x,y,dx,dy,depth):
		Err=1
		# calc reflect ray
		sdf=self.objects.sdf
		gy=(sdf(x+Err,y)[0]-sdf(x-Err,y)[0])/2/Err
		gx=(sdf(x,y+Err)[0]-sdf(x,y-Err)[0])/2/Err
		dx-=2*(dx*gx+dy*gy)*gx
		dy-=2*(dx*gx+dy*gy)*gy
		norm=(dx**2+dy**2)**0.5
		dx/=norm
		dy/=norm
		# call trace method
		return self.trace(x+1.2*gx*Err,y+1.2*gy*Err,dx,dy,depth-1)
	def trace_refract(self,x,y,dx,dy):
		Err=1
		# calc reflect ray
		sdf=self.objects.sdf
		gy=(sdf(x+Err,y)[0]-sdf(x-Err,y)[0])/2/Err
		gx=(sdf(x,y+Err)[0]-sdf(x,y-Err)[0])/2/Err
		n=2 # temporary value
		(hx,hy)=(dx+gx)/n,(dy+gy)/n
		norm=(dx**2+dy**2-hx**2-hy**2)**0.5
		gx=norm*gx+hx
		gy=norm*gy+hy
		# call trace method
		return self.trace(x-1.2*gx*Err,y-1.2*gy*Err,dx,dy,depth-1)
	def reset(self):
		self.objects=Obj(-1)
	def scene_0(self):
		# self.objects=Obj(2,[200,200,0.5,0.5,Color.white()])
		# self.objects=Obj(3,[250,220,180,140,100,300,Material(color=Color.black(),illu=0,reflect=1,refract=0)])+Obj(0,[100,100,50,Material(color=Color.red(),illu=1)])
		self.objects=Obj(3,[100,150,125,150,125,0,Material(reflect=1)])+Obj(3,[175,0,175,150,200,150,Material(reflect=1)])+Obj(3,[0,150,300,300,150,250,Material(reflect=1)])+Obj(0,[150,0,25,Material(color=Color.white(),illu=1)])+Obj(0,[20,280,30,Material(color=Color.blue(),illu=1)])
		# self.objects=Obj(0,[100,100,50,Color.white()])+Obj(0,[150,190,50,Color.black()])+Obj(1,[200,200,0.5,0.5,Color.white()])
	def scene404(self):
		self.reset()
		pass