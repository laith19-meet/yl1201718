from turtle import *
import turtle 
import time 
import random
from ball import Ball
tracer (0)
hideturtle()
RUNNING = True 
SLEEP=0.0077
SCREEN_WIDTH=getcanvas().winfo_width()/2
SCREEN_HEIGHT=getcanvas().winfo_width()/2
MY_BALL=Ball(12,12,10,15,23,"blue")
NUMBER_OF_BALLS= 5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

random.randint(0,10)
balls = []

for i in range(NUMBER_OF_BALLS):
	X=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	print (dx)

	if dx == 0 :
		dx += 1

	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	print (dy)

	if dy == 0 : 
		dy +=0 

	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	print(radius)

	color = (random.random() , random.random(), random.random())
	print (color)
	new_ball= Ball(x,y,dx,dy,radius,color)
	balls.append(new_ball)

	while True:
		for ball in balls:
			ball.move(SCREEN_WIDTH,SCREEN_WIDTH)

def collide(ball_a, ball_b):
	if ball_a == ball_b :
		return False 

	if (math.sqrt(math.pow(ball_a.x- ball_b.x)) + (math.pow(ball_a.y - ball_b.y))):
		return True
	else :
		return False

def check_all_balls_collision(self):
	for ball_a in (balls):
		for ball in (balls): 
			if collide(ball_a,ball_b) == True:
				ball_a_radius = ball_a.r()
				ball_b_radius = ball_b.r()
				if ball_a . ball_a_radius > ball_b_radius :
					ball_a_radius=+1
				else : 
					ball_b_radius =+ 1

		X_COORDINATE = random.randint(round(-SCREEN_WIDTH) , round(SCREEN_WIDTH))
		Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT) , round(SCREEN_HEIGHT))
		X_AXISSPEED = random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		Y_AXISSPEED = random.randint( MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

		while X_AXISSPEED and Y_AXISSPEED == 0 :
			X_AXISSPEED= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			Y_AXISSPEED= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			print(radius)

			color = (random.random(), random.random() , random.random())
			print(color)

		if ball_a.r > ball_b.r :
			ball_b.r = radius 
			ball_b.x = X_COORDINATE
			ball_b.Y = Y_COORDINATE
			ball_b.dx = X_AXISSPEED
			ball_b.dy = Y_AXISSPEED
			ball_b.color(color)
			ball_b.shapesize(ball_b.r/10)
			ball_a.r =ball_a.r+1
			ball_a.shapesize(ball_a.r/10)

		else:
			ball_a.r = radius 
			ball_a.x = X_COORDINATE
			ball_a.Y = Y_COORDINATE
			ball_a.dx = X_AXISSPEED
			ball_a.dy = Y_AXISSPEED
			ball_a.shapesize(ball_a.r/10)
			ball_b.r =ball_b.r+1
			ball_b.shapesize(ball_b.r/10)

def check_myball_collision ():
	for ball in balls :
		if collide(MY_BALL,ball) == True:
			ball_r4 = ball.r
			my_ball_r4 = ball.r
			if my_ball_r4 >= ball_r4:

				return False

				X_COORDINATE = random.randint(round(-SCREEN_WIDTH) , round (SCREEN_WIDTH))
				Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT) , round(SCREEN_HEIGHT))
				X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_AXISSPEED = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while X_AXISSPEED and Y_AXISSPEED == 0: 
					X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
					Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				print (radius)

				color = (random.random(), random.random() , random.random())
				
				print(color)	


mainloop()			



