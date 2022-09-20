#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# Set legs to the number of legs you want on your spider
legs = 6
# Set length to the length you want for the legs
length = 70
# Set angle to the direction you want your legs to go out
angle = 380 / legs
spider.pensize(5)
# Set count to make it less than legs to activate the loop for a certain period
count = 0
while (count < legs):
  spider.goto(0,0)
  spider.setheading(angle*count)
  spider.forward(length)
  count = count + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()