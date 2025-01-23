import turtle

windows = turtle.getscreen()
# orqa fon qismi
turtle.hideturtle()
windows.bgcolor("#0049FF")
t = turtle.Turtle()
t.speed(0)

# sohil qismi
t.up()
t.goto(-765, 0)
t.down()
t.speed(0)
t.color("#DDD69B")
t.begin_fill()
for i in range(2):
    t.forward(1525)
    t.right(90)
    t.forward(392)
    t.right(90)
t.end_fill()

# osmon
t.up()
t.goto(-765, 400)
t.down()
t.color("#A7CBFF")
t.begin_fill()
for i in range(2):
    t.forward(1525)
    t.right(90)
    t.forward(190)
    t.right(90)
t.end_fill()

# quyosh
t.up()
t.goto(570, 300)
t.down()
t.color("yellow")
t.pensize(10)
t.dot(110, "yellow")
for i in range(8):
    t.left(45)
    t.forward(100)
    t.backward(100)
t.left(40)


# qush shakli
def bird(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.left(90)
    t.color("black")
    t.circle(40, 120)
    t.left(40)
    t.circle(-40, -120)


bird(-400, 280)
bird(-520, 340)
bird(-560, 260)
t.right(20)


# akula shakli
def shark(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.left(30)
    t.fillcolor("#B0ACAB")
    t.begin_fill()
    t.circle(50, 60)
    t.left(50)
    t.circle(50, -98)
    t.right(40)
    t.end_fill()


shark(-100, 100)
shark(-10, 140)
shark(100, 70)
t.left(100)


# daraxt shakli
def tree(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor("#A0522E")
    t.begin_fill()
    t.left(95)
    t.circle(-500, -55)
    t.left(160)
    t.circle(510, -55)
    t.end_fill()
    t.left(110)


tree(-500, -390)
tree(580, -390)
t.right(130)


# daraxzt barglari
def leaf(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor("#97CD32")
    t.begin_fill()
    for _ in range(2):
        t.left(160)
        t.circle(100, -120)
        t.right(25)
        t.circle(110, 150)
        t.setheading(100)
    t.left(170)
    for _ in range(3):
        t.left(40)
        t.circle(-110, -120)
        t.right(30)
        t.circle(-110, 80)
    t.circle(-110, 50)
    t.end_fill()
    t.left(30)


leaf(-530, 0)
leaf(520, 0)

# # bulut
t.up()
t.goto(0, 260)
t.down()
t.color("white")
t.begin_fill()
for _ in range(3):
    t.circle(60)
    t.right(50)
t.end_fill()
t.left(200)


# # soyabon
def umbrella(x, y):
    t.color("black")
    t.up()
    t.goto(x, y)
    t.down()
    t.forward(120)
    t.pensize(2)
    t.fillcolor("#FC0000")
    t.begin_fill()
    t.right(60)
    t.forward(80)
    t.left(90)
    t.circle(80, 180)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.up()
    t.forward(80)
    t.dot(10)
    t.left(145)
    t.down()
    t.forward(96)
    t.backward(96)
    t.end_fill()
    t.fillcolor("white")
    t.begin_fill()
    t.left(22)
    t.forward(83)
    t.right(77)
    t.forward(37)
    t.right(124)
    t.forward(96)
    t.right(130)
    t.forward(83)
    t.left(77)
    t.forward(37)
    t.left(124)
    t.forward(96)
    t.end_fill()
    t.pensize(10)
    t.right(67)


umbrella(-110, -210)
umbrella(-300, -350)
umbrella(100, -350)
t.hideturtle()

windows.mainloop()
