import turtle
turtle.getscreen()
turtle.Screen().bgcolor("#090145")
t=turtle.Turtle()
t.speed(10000)

def snowflake(size):
 
    t.penup()
    t.forward(10*size)
    t.left(45)
    t.pendown()
    t.color("white")
 
    for i in range(8):
        branch(size)  
        t.left(45)
     
 
def branch(size):
    for i in range(3):
        for i in range(3):
            t.forward(10.0*size/3)
            t.backward(10.0*size/3)
            t.right(45)
        t.left(90)
        t.backward(10.0*size/3)
        t.left(45)
    t.right(90)
    t.forward(10.0*size)
    

def star(size,c):
  t.color(c)
  t.begin_fill()
  for i in range(5):
    t.forward(size*15)
    t.right(144)
  t.end_fill()
  
# Background
t.penup()
t.goto(-250,-125)
t.pendown()

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
for i in range(4):
  t.forward(500)
  t.right(90)
t.end_fill()

t.penup()
t.goto(68,-125)
t.pendown()

# Christmas Tree
t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.left(90)
  t.forward(130)
  t.left(90)
t.end_fill()

t.penup()
t.goto(10,-100)
t.pendown()

t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(160)
  t.left(90)
  t.forward(40)
  t.left(90)
t.end_fill()

t.penup()
t.goto(30,-60)
t.pendown()

t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(120)
  t.left(90)
  t.forward(40)
  t.left(90)
t.end_fill()

t.penup()
t.goto(50,-20)
t.pendown()

t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(80)
  t.left(90)
  t.forward(40)
  t.left(90)
t.end_fill()

t.penup()
t.goto(70,20)
t.pendown()

t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(40)
  t.left(90)
  t.forward(40)
  t.left(90)
t.end_fill()

t.penup()
t.goto(80,60)
t.pendown()

t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(20)
  t.left(90)
  t.forward(40)
  t.left(90)
t.end_fill()

t.penup()
t.goto(55,110)
t.pendown()

star(14/3,"yellow")

# Snowman
t.penup()
t.goto(-100,-130)
t.pendown()

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-100,-35)
t.pendown()

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-148,-60)
t.pendown()

t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.goto(-180,-30)
t.goto(-178,-27)
t.goto(-146,-58)
t.goto(-148,-60)
t.end_fill()

t.penup()
t.goto(-52,-60)
t.pendown()

t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.goto(-10,-30)
t.goto(-12,-27)
t.goto(-54,-58)
t.goto(-52,-60)
t.end_fill()

t.penup()
t.goto(-100,-55)
t.pendown()

t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.dot(20)
t.end_fill()

t.penup()
t.goto(-100,-75)
t.pendown()

t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.dot(20)
t.end_fill()

t.penup()
t.goto(-100,-95)
t.pendown()

t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.dot(20)
t.end_fill()

t.penup()
t.goto(-115,15)
t.pendown()

t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(-85,15)
t.pendown()

t.pencolor("black")
t.fillcolor("black")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(-100,5)
t.pendown()

t.pencolor("orange")
t.fillcolor("orange")
t.begin_fill()
t.goto(-72,1)
t.goto(-100,-3)
t.goto(-100,5)
t.end_fill()

t.penup()
t.goto(-134,30)
t.pendown()

t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
for i in range(3):
  t.forward(68)
  t.left(120)
t.end_fill()

t.penup()
t.goto(-100,74)
t.pendown()

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(12)
t.end_fill()

t.penup()
t.goto(83,58)
t.pendown()

# Decoration On Christmas Tree
star(1,"#05fafa")

t.penup()
t.goto(80,35)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(100,35)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(55,12)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(89,12)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(110,12)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(117,-8)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(83,-8)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(63,-8)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(38,-30)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(75,-30)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(108,-30)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(127,-30)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(60,-50)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(83,-50)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(122,-50)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(18,-78)
t.pendown()

star(1,"#05fafa")
t.penup()
t.goto(53,-78)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(72,-78)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(97,-78)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(129,-78)
t.pendown()

t.pencolor("#fa05f6")
t.fillcolor("#fa05f6")
t.begin_fill()
t.dot(15)
t.end_fill()

t.penup()
t.goto(148,-78)
t.pendown()

star(1,"#05fafa")

t.penup()
t.goto(-150,-130)
t.pendown()

# "Merry Christmas" (word) 
t.pencolor("red")

# M
t.right(90)
t.forward(30)
t.backward(30)
t.goto(-140,-150)
t.goto(-130,-130)
t.forward(30)

t.penup()
t.goto(-120,-130)
t.pendown()

# E
t.forward(30)
for i in range(2):
  t.left(90)
  t.forward(15)
  t.backward(15)
  t.right(90)
  t.backward(15)
t.left(90)
t.forward(15)
t.backward(15)

t.penup()
t.goto(-95,-130)
t.pendown()

# R
t.right(90)
t.forward(30)
t.backward(30)
t.left(90)
for i in range(3):
  t.forward(15)
  t.right(90)
t.goto(-80,-160)

t.penup()
t.goto(-70,-130)
t.pendown()

# R
t.right(90)
t.right(90)
t.forward(30)
t.backward(30)
t.left(90)
for i in range(3):
  t.forward(15)
  t.right(90)
t.goto(-55,-160)

t.penup()
t.goto(-45,-130)
t.pendown()

# Y
t.goto(-35,-145)
t.goto(-25,-130)
t.goto(-35,-145)
t.backward(15)

t.penup()
t.goto(-95,-165)
t.pendown()

# C
t.right(90)
t.forward(15)
t.backward(15)
t.right(90)
t.forward(30)
t.left(90)
t.forward(15)

t.penup()
t.goto(-70,-165)
t.pendown()

# H
t.right(90)
t.forward(30)
t.backward(15)
t.left(90)
t.forward(15)
t.right(90)
t.forward(15)
t.backward(30)

t.penup()
t.goto(-45,-165)
t.pendown()

# R
t.forward(30)
t.backward(30)
t.left(90)
for i in range(3):
  t.forward(15)
  t.right(90)
t.goto(-30,-195)

t.penup()
t.goto(-20,-165)
t.pendown()

# I
t.right(90)
t.forward(15)
t.backward(7.5)
t.right(90)
t.forward(30)
t.left(90)
t.forward(7.5)
t.backward(15)

t.penup()
t.goto(5,-165)
t.pendown()

# S
t.forward(15)
t.backward(15)
t.right(90)
t.forward(15)
t.left(90)
t.forward(15)
t.right(90)
t.forward(15)
t.right(90)
t.forward(15)

t.penup()
t.goto(30,-165)
t.pendown()

# T
t.backward(15)
t.forward(7.5)
t.left(90)
t.forward(30)

t.penup()
t.goto(55,-165)
t.pendown()

# M
t.forward(30)
t.backward(30)
t.goto(65,-185)
t.goto(75,-165)
t.forward(30)

t.penup()
t.goto(95,-165)
t.pendown()

# A
t.goto(85,-195)
t.goto(95,-165)
t.goto(105,-195)
t.goto(100,-180)
t.goto(90,-180)

t.penup()
t.goto(115,-165)
t.pendown()

# S
t.left(90)
t.forward(15)
t.backward(15)
t.right(90)
t.forward(15)
t.left(90)
t.forward(15)
t.right(90)
t.forward(15)
t.right(90)
t.forward(15)

t.penup()
t.goto(160,-150)
t.pendown()

star(2,"#f7023c")

t.penup()
t.goto(-150,-185)
t.pendown()

star(2,"#f7023c")

#different snowflakes
t.penup()
t.goto(-150,150)
t.pendown()

snowflake(2)
branch(2)

t.penup()
t.goto(-50,170)
t.pendown()

snowflake(1.5)
branch(1.5)

t.penup()
t.goto(-45,100)
t.pendown()
t.right(180)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()

t.left(90)

for i in range (0,6):
  t.forward(25)
  t.forward(-10)
  t.left(40)
  t.forward(7)
  t.forward(-7)
  t.right(80)
  t.forward(7)
  t.forward(-7)
  t.left(40)
  t.forward(-15)
  
  t.right(60)

t.end_fill()

t.penup()
t.goto(50,150)
t.pendown()
t.right(180)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()

t.left(90)

for i in range (0,6):
  t.forward(25)
  t.forward(-10)
  t.left(40)
  t.forward(7)
  t.forward(-7)
  t.right(80)
  t.forward(7)
  t.forward(-7)
  t.left(40)
  t.forward(-15)
  
  t.right(60)

t.end_fill()

t.penup()
t.goto(130,165)
t.pendown()

snowflake(1.5)
branch(1.5)

t.penup()
t.goto(4,30)
t.pendown()
t.right(180)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()

t.left(90)

for i in range (0,6):
  t.forward(25)
  t.forward(-10)
  t.left(40)
  t.forward(7)
  t.forward(-7)
  t.right(80)
  t.forward(7)
  t.forward(-7)
  t.left(40)
  t.forward(-15)
  
  t.right(60)

t.end_fill()

t.penup()
t.goto(177,100)
t.pendown()

snowflake(2)
branch(2)

t.penup()
t.goto(30,85)
t.pendown()

snowflake(1)
branch(1)

t.penup()
t.goto(-162,65)
t.pendown()

snowflake(1)
branch(1)