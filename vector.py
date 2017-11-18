import operator

__author__ = 'tabokie'

class Vector3d(object):
	def __init__(self,x,y,z):
		(self.x,self.y,self.z)=x,y,z
	def _operation(self,other,op):
		(x,y,z)=op(self.x,other.x),op(self.y,other.y), op(self.z,other.z)
		return Vector3d(x,y,z)
	def __add__(self,other):
		return self._operation(other,operator.add)
	def __mul__(self,other):
		return self._operation(other,operator.mul)
	def __sub__(self,other):
		return self._operation(other,operator.sub)
