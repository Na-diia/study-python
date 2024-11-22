import turtle

def drawSquare(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()
    def move(len):
        turtle.forward(len)
        turtle.left(90)
    for _ in range(4):
        move(size)
    turtle.end_fill()

drawSquare(100, 'yellow')
turtle.goto(100, 100)
drawSquare(100, 'blue')
