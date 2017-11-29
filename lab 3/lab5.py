from turtle import *
import random 
colormode(255)
class Square(Turtle):
	def __init__(self,size, shape):
		Turtle.__init__(self)
		self.shapesize= (12)
		self.shape (shape)
	def random_color(self):
		r =random.randint(0 , 256)
		g =random.randint(0 , 256)
		b =random.randint(0 , 256)
		self.color(r ,g ,b )

square1 = Square(2, 'square')
square1.random_color()


class rectangile(Turtle):
	def __init__ (self,height, width):
		Turtle.__init__(self)
		self.height = height
		self.width = width
		register_shape("name",((width,height),(width,height+50),(width+150-(50),height+50),(width+150-(50),height-50),(width,height-50)))
		self.shape("name")
		self.setheading(90)
		self.setheading(180)
		self.setheading(270)
		self.setheading(360)
		self.setheading(90)

my_rectangile=rectangile(100,0)

class square(rectangile):
		def __init__ (self,size):
			rectangile.__init__(self,size, size)
			#register_shape("hey",((width,height),(width,height+50),(width+100,height+50),(width+100,height-50),(width,height-50)))
			#self.shape("hey")

my_square=square(-100)

mainloop()