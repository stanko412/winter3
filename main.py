import turtle


screen=turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('beige')

t = turtle.Turtle()
t.pencolor("black")
t.speed(2)

t_ground=turtle.Turtle()
t_ground.speed(0)
t_ground.pencolor('brown')
t_ground.fillcolor('brown')

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-100)

t_ground.end_fill()

t.speed(0)


t.penup()
t.goto(21, -98)
t.pendown()
t.fillcolor("chocolate4")
t.begin_fill()
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()




t.pencolor("green")

t.penup()
t.goto(-80, -10)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.goto(80, 0)
t.goto(0, 60)
t.goto(-80, 0)
t.end_fill()


t.penup()
t.goto(-80, 70)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.goto(80, 80)
t.goto(0, 140)
t.goto(-80, 80)
t.end_fill()

#
t.penup()
t.goto(-80, 30)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.goto(80, 40)
t.goto(0, 100)
t.goto(-80, 40)
t.end_fill()

t.penup()
t.goto(-200, 50)
t.pendown()
t.fillcolor("beige")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()




t.penup()
t.goto(-250, 55)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()


t.penup()
t.goto(-250, 80)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(15)
t.end_fill()


t.penup()
t.goto(-250, 100)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-254, 108)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-246, 108)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-250, 103)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.pencolor("black")
t.goto(-250, 150)
t.pendown()
t.setheading(270)
t.forward(100)
t.penup()

t.goto(-300, 100)
t.pendown()
t.pencolor("black")
t.setheading(0)
t.forward(100)

t.hideturtle()


t.penup()
t.color("light blue")
t.fillcolor("light blue")
t.goto(30, 5)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()


t.penup()
t.color("maroon")
t.fillcolor("maroon")
t.goto(25, 40)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.color("purple")
t.fillcolor("purple")
t.goto(-35, 0)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()


t.penup()
t.color("white")
t.fillcolor("white")
t.goto(-25, 80)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.color("magenta")
t.fillcolor("magenta")
t.goto(-30, 40)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.color("silver")
t.fillcolor("silver")
t.goto(20, 80)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()


star = turtle.Turtle()
star.penup()
star.goto(-25, 145)
star.pendown()
t.hideturtle()
star.pencolor("yellow")
star.fillcolor('yellow')
star.begin_fill()

for i in range(5):
    star.forward(50)
    star.right(144)

star.end_fill()



t.hideturtle()

t.fillcolor('red')
t.begin_fill()
t.penup()
t.pendown()

t.penup()
t.goto(-80, -50)
t.pendown()

t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()

t.fillcolor('purple')
t.begin_fill()
t.penup()
t.pendown()

t.penup()
t.goto(-140, -50)
t.pendown()

t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()



t.penup()
t.goto(245, 175)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.end_fill()

t.penup()
t.goto(90, 130)  # Start position for the first rectangle
t.pendown()
t.fillcolor("black")
t.begin_fill()

# Draw the first rectangle
t.left(30)
t.forward(60)
t.left(60)
t.forward(30)
t.left(120)
t.forward(60)
t.left(60)
t.forward(30)

t.end_fill()


t.penup()
t.goto(190, 130)
t.pendown()
t.fillcolor("black")
t.begin_fill()

#
t.setheading(150)

#
t.forward(60)
t.left(60)
t.forward(30)
t.left(120)
t.forward(60)
t.left(60)
t.forward(30)
t.end_fill()

t.hideturtle()
t.penup()
t.goto(25,200)
t.write("Merry Christmas", font=("Arial", 60, "bold"), align="center")


#last line of code
turtle.done()



