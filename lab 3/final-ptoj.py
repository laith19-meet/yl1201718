from turtle import *
import random
import time

colormode(255)
#tracer(0)
hideturtle()

SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HIGHT = getcanvas().winfo_height()/2

right_side_ball = 0
left_side_ball = 0
up_side_ball = 0
down_side_ball = 0
class Circle(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)


		def random_color(self):
			r =random.randint(0,255) 

			g =random.randint(0,255) 

			b =random.randint(0,255)

			self.color(r,g,b)

	def move (self,width,hight):
		current_x = self.xcor()
		new_x= current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy 
		global right_side_ball
		global left_side_ball
		global up_side_ball
		global down_side_ball
		right_side_ball= new_x + new_y/2
		left_side_ball = new_x - new_y/2
		up_side_ball = new_y + new_x/2
		down_side_ball = new_y + new_x/2
		self.goto(new_x,new_y)
#pd()
circle1 = Circle(20,0 ,.3,.2,20,"red")
circle2 = Circle(-100,0,0.1, 0.2,20,"blue")
circle1.move(SCREEN_WIDTH,SCREEN_HIGHT)
while True :
	circle1.move(SCREEN_WIDTH,SCREEN_HIGHT)
	circle2.move(SCREEN_WIDTH,SCREEN_HIGHT)
	getscreen().update()
	time.sleep(0.01)

if circle1.pos() <= SCREEN_HIGHT:
	circle1.move(-.3,-.2)
if circle1.pos() <= SCREEN_WIDTH:
	circle1.move(.3,.2)

mainloop()



