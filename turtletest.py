import turtle
# def turtle1():
#     turtle.showturtle()
#     turtle.write("hello python")
#     turtle.forward(100)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.forward(100)
#     turtle.mainloop()

def turtle2():
    turtle.goto(100,100)
    turtle.goto(100,-100)
    turtle.goto(-100,-100)
    turtle.goto(-100,100)
    turtle.goto(100,100)
    turtle.goto(200,200)
    turtle.penup()
    # turtle.penup(200,-200)
    turtle.goto(200,-200)
    turtle.goto(-200,-200)
    turtle.pendown()
    turtle.goto(200,200)
    turtle.color('red')
    turtle.goto(-200,200)
    turtle.color('yellow')
    turtle.goto(-200,-200)
    turtle.color('blue')
    turtle.goto(0,0)
    turtle.circle(100)
    turtle.circle(200)




    turtle.mainloop()
if __name__ == '__main__':
    turtle2()
# turtle1()