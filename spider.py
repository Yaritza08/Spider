#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# Create a Spider Body!
# Select a pen size!
spider.pensize(40)
# Create a circle!
spider.circle(20)

# Set legs to the number of legs you want on your spider
legs = 4
# Set length to the length you want for the legs
length = 70
# Set angle to the direction you want your legs to go out
angle1 = 100 / legs
angle2 = -100 / legs
spider.pensize(5)
# Set count to make it less than the number of legs to activate the loop
#The loop will run from count until it reaches the number of legs - Choose a count depending on how many loops you want the program to run
count = 0
while (count < legs):
  spider.goto(0,20) # Set coordinates to the center of the spider's body
  spider.setheading(angle1*count-100) #This is the direction of the legs
  spider.forward(length) # How long it goes forward
  count = count + 1 # Creating increments
spider.hideturtle() # So the turtle doesn't draw as you go back to the original coordinates
count=0
while (count < legs):
  spider.goto(0,20) # Set coordinates to the center of the spider's body
  spider.setheading(angle1*count+100) #This is the direction of the legs
  spider.forward(length) # How long it goes forward
  count = count + 1 # Creating increments
spider.hideturtle()

spider.penup()
spider.goto(-10,0)
spider.pendown()
spider.pencolor('white')
spider.pensize(5)
# Create a circle!
spider.circle(2)
spider.penup()
spider.goto(-24, 15)
spider.pendown()
spider.circle(2)
wn = trtl.Screen()
wn.mainloop()