from vector import Vector3d

__author__ = 'tabokie'

class Scene3d(object):
	def __init__(self,viewcode,layoutcode):
		setView(viewcode)
		setLayout(layoutcode)
	# receive (x,y) on canvas
	# return direction vector3d
	def viewRay(self,x,y):

	def setView(self,viewcode):

	def setLayout(self,layoutcode):

	# receive starting point:(x,y) and direction dv
	# return intersect point vector3d
	def intersect(self,x,y,dv):

	# receive intersect point v and view direction dv
	# return sample color
	def layoutSampling(self,v,dv):
		# nature color
		# trace in all directions
		initColor=trace(v)
		# highlight
		# 
		reflect=trace_reflect(v,dv)
		# refract
		refract=trace_refract(v,dv)
		# compose

	def layoutShading(self,v,dv):
		# nature color
		# compose all lighting
		initColor=lambertianShading(v)
		#highlight
		highlight=blinn_phongShading(v,dv)

	def sample(self,x,y):
		dv=viewRay(x,y)
		v=intersect(x,y,dv)
		layoutSampling(v,dv)