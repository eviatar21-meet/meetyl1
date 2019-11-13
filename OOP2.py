from turtle import Turtle
import turtle
class  Ball(Turtle):
	def __init__ (self,r,color,dx,dy):
		Turtle.__init__(self) 
		self.penup()
		self.dx =dx
		self.dy =dy
		self.shape("circle")
		self.color(color)
		self.r = r/10

	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		newX = current_x + self.dx
		current_y = self.ycor()
		newY = current_y + self.dy
		right_side_ball = newX + self.r
		left_side_ball = newX - self.r
		upper_side_ball = newY + self.r
		lower_side_ball = newY - self.r
		if right_side_ball>screen_width:
			self.dx = -self.dx
		if left_side_ball< -screen_width:
			self.dx = -self.dx 
		if lower_side_ball< -screen_height:
			self.dy = -self.dy
		if upper_side_ball>screen_height:
			self.dy = -self.dy
		self.goto(newX,newY)

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

ball1 = Ball(10,"blue",10,10)

while 1==1:
	ball1.move(screen_width,screen_height)


