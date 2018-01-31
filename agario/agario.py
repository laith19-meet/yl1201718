from turtle import *	
import turtle 
import time 
import random
from ball import Ball

bgcolor("black")
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

balls = []

for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

	if dx == 0 :
		dx += 1

	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

	if dy == 0 : 
		dy +=1 



	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)


	color = (random.random() , random.random(), random.random())
	ball= Ball(x,y,dx,dy,radius,color)
	balls.append(ball)
def move_all_balls ():
	for ball in balls:
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a, ball_b):
	if ball_a == ball_b :
		return False 

	balls_distance = ((ball_a.xcor() - ball_b.xcor())**2  + (ball_a.ycor() - ball_b.ycor())**2 )**0.5

	if balls_distance + 10 <= ball_a.radius + ball_b.radius:
		return True 
	else:
		return False


def check_all_balls_collision():
	for ball_a in (balls):
		for ball_b in (balls): 
			if collide(ball_a,ball_b) == True:
				ball_a_radius = ball_a.radius
				ball_b_radius = ball_b.radius
				if ball_a.radius > ball_b.radius :
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


		color = (random.random(), random.random() , random.random())


		if ball_a.radius > ball_b.radius :
			ball_b.r = radius 
			ball_b.x = X_COORDINATE
			ball_b.Y = Y_COORDINATE
			ball_b.dx = X_AXISSPEED
			ball_b.dy = Y_AXISSPEED
			ball_b.color(color)
			ball_b.shapesize(ball_b.r/10)
			ball_a.radius =ball_a.radius+1
			ball_a.shapesize(ball_a.radius/10)

		else:
			ball_a.r = radius 
			ball_a.x = X_COORDINATE
			ball_a.Y = Y_COORDINATE
			ball_a.dx = X_AXISSPEED
			ball_a.dy = Y_AXISSPEED
			ball_a.shapesize(ball_a.radius/10)
			ball_b.radius =ball_b.radius+1
			ball_b.shapesize(ball_b.radius/10)

def check_myball_collision ():
	for ball in balls :
		if collide(MY_BALL,ball) == True:
			ball_radius4 = ball.radius
			my_ball_radius4 = ball.radius
			if my_ball_radius4 >= ball_radius4:

				return False

				X_COORDINATE = random.randint(round(-SCREEN_WIDTH) , round (SCREEN_WIDTH))
				Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT) , round(SCREEN_HEIGHT))
				X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_AXISSPEED = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while X_AXISSPEED and Y_AXISSPEED == 0: 
					X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
					Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)


				color = (random.random(), random.random() , random.random())
				
	


def movearound(event):
	x_cord=event.x- SCREEN_WIDTH
	y_cord=  SCREEN_HEIGHT - event.y 
	MY_BALL.goto(x_cord, y_cord)

turtle.getcanvas().bind("<Motion>", movearound)
getscreen().listen()

while RUNNING == True  :
	if SCREEN_WIDTH != getcanvas().winfo_width()/2 or SCREEN_HEIGHT != getcanvas().winfo_height()/2 :
		SCREEN_WIDTH = getcanvas().winfo_width()/2
		SCREEN_HEIGHT = getcanvas().winfo_height()/2


	move_all_balls()
	check_all_balls_collision()
	if check_myball_collision() == True :
		RUNNING = True

	else :
		RUNNING = False
	getscreen().update()
	time.sleep(SLEEP)

mainloop()

