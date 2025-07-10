import turtle
turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(300,400)
turtle.title("Square Spiral!")
pen = turtle.Turtle()
angle = 0
while True:
    for j in range(4):
        pen.forward(angle+1)
        pen.right(90)
        angle -= 5 
    angle += 1
turtle.done()