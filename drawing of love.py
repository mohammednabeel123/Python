import turtle

def draw_heart():
    turtle.color("red")
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

if __name__ == "__main__":
    turtle.speed(2)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    draw_heart()
    turtle.hideturtle()
    turtle.done()