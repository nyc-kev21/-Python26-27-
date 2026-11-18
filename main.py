from myFunction import *


from random import *

turtle.colormode(255)

bob.speed(0)
bob.width(2)

turtle.bgcolor("cyan")


num = randint(10, 20)

for times in range(1050):

  x = randint(-250, 250)
  y = randint(-250, 250)

  jump(x, y)

  border = (randint(0,255), randint(0,255), randint(0,255))
  fill = (randint(0,255), randint(0,255), randint(0,255))

  circle(randint(10, 35), border, fill)
