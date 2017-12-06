from turtle import *
import random
import math
class ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

circle1= ball(25,"black",6)
circle1.pu()
circle1.forward(100)
circle1.pd()
circle2= ball(20,"blue",9)
circles= []
circles.append(circle1)
circles.append(circle2)
print(circles)

def check_collision(circle1, circle2):
	x1=circle1.xcor()
	y1=circle1.ycor()
	x2=circle2.xcor()
	y2=circle2.ycor()
	b=math.pow(x2-x1)
	xsquared= math.sqrt(b)
	f=math.pow(y2-y1)
	ysquared=math.sqrt(d)
	z=b+f
	d=math.sqrt(z)
	print(d)
	
	


mainloop()