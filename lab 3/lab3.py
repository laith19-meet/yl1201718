import turtle
import random
strait = 100
circul= 145
colors  = ["red","green","blue","orange","purple","pink","yellow"]
for i in range(5):
	turtle.forward(strait)
	turtle.right(circul)
	color = random.choice(colors)
	turtle.color(color)

turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(270)
turtle.forward(20)
turtle.right(320)
turtle.forward(20)
turtle.right(270)
turtle.forward(20)
turtle.mainloop()
