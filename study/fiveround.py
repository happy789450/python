import turtle
def round1():
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()

def fiveround1():
    turtle.penup()
    turtle.goto(-100,0)
    turtle.color('red')
    round1()
    turtle.goto(120,0)
    turtle.color('yellow')
    turtle.pendown()
    round1()
    turtle.goto(340,0)
    turtle.color('blue')
    round1()
    turtle.goto(-10,-90)
    turtle.color('red')
    round1()
    turtle.goto(240,-90)
    turtle.color('green')
    round1()
    turtle.done





if __name__ == '__main__':
    fiveround1()