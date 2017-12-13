from turtle import *
import random
import math
class rectangule(Turtle):
	def __init__(self, width , height , x,y):
		Turtle.__init__(self)
		register_shape("rectangule", ((x+60,y),(x+60,y+40),(x-60,y+40),(x-60,y-40)))
		self.shapesize(width/10,height/10,1)
		self.width = width
		self.height = height
		self.goto(x,y)
Right = height + width/2
Left = height - width/2
Bottom = width + height/2
Top = width - height/2

A= rectangule(5,7,9,0)
B= rectangule(5,7,12,0)
rectangules=[]
rectangules.append(A)
rectangules.append(B)
print(rectangules)

def check_collision():
	if(
	A.Top() >= B.Bottom()and
	A.Right() >= B.Left()and
	A.Bottom() <= B.Top()and
	A.Left() <= B.Right()
	):

		print("collisions")
check_collision()
mainloop()
