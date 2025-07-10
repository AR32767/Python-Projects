import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,400)
pen = turtle.Turtle()
sides = 6
length = 170
pen.up()
pen.goto(170,170)
pen.down()
angle= 360/sides
for i in range(sides):
    pen.forward(length)
    pen.right(angle)
turtle.done()

