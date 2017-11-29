from turtle import *
def polygon(n,side_length):
	for i in range (n):
		left(360/n)
		forward(side_length)

polygon(6,100)

mainloop()