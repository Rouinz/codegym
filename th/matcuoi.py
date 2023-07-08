import turtle
t = turtle.Turtle()
#face
t.pensize(5)
fs = 100
t.circle(fs)
t.penup()
t.goto(-40,100)
t.pendown()
#eyes
eyes = 30
t.pensize(2)
t.circle(eyes)
t.penup()
t.goto(40,100)
t.pendown()
t.circle(eyes)
#nose
t.penup()
t.goto(0,100)
t.pendown()
t.circle(-20,steps=3)
#mouth
t.penup()
t.goto(-40,50)
t.pendown()
t.right(90)
t.circle(40,180)
turtle.done()