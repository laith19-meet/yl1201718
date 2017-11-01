##problem 1
print("laith ")*100

##problem 2 (a)
number1=100
print(number1)

##problem 2 (b)
number2=number1/2
print(number2)

##problem 3 (a)
sum=0
for i in [10,20,30]:
	print(i)
	
	##problem 3 (b)
	print(i)*2

	##problem 3 (c)
	sum=sum+i
print(sum)
##problem 4
radius=50
import turtle 
turtle.penup()
turtle.begin_fill()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.end_fill()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.write("did you like my box?")
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
turtle.begin_fill()
turtle.pensize(20)
turtle.circle(radius)
turtle.mainloop()