import turtle
#set up
udh = turtle.Turtle()
udh.speed(1000)
def go(x,y):
    udh.penup()
    udh.goto(x,y)
    udh.pendown()
#housing
udh.fillcolor('#708090')
udh.begin_fill()
for i in range(2):
    udh.forward(300)
    udh.right(90)
    udh.forward(150)
    udh.right(90)
udh.end_fill()
go(130,-150)
udh.left(90)
udh.fillcolor('#57DD73')
udh.begin_fill()
for i in range(2):
    udh.forward(70)
    udh.right(90)
    udh.forward(40)
    udh.right(90)
udh.end_fill()
go(0,0)
udh.fillcolor('#57DD73')
udh.begin_fill()
udh.right(45)
udh.forward(177)
udh.right(90)
udh.forward(177)
udh.end_fill()
go(200,50)
udh.fillcolor('#BB4732')
udh.begin_fill()
udh.left(135)
udh.forward(20)
udh.right(90)
udh.forward(25)
udh.right(90)
udh.forward(47)
udh.end_fill()
#tree
go(-200,-200)
udh.fillcolor('#3F2A32')
udh.begin_fill()
udh.left(175)
udh.forward(60)
udh.right(85)
udh.forward(10)
udh.right(85)
udh.forward(60)
udh.right(95)
udh.forward(20)
udh.end_fill()
udh.right(180)
go(-218,-140)
udh.fillcolor('#1E6649')
udh.begin_fill()
udh.forward(60)
udh.left(90+35)
udh.forward(56)
udh.left(110)
udh.forward(56)
udh.end_fill()
go(-213,-94)
udh.fillcolor('#1E6649')
udh.begin_fill()
udh.right(55+180)
udh.forward(50)
udh.left(90+35)
udh.forward(46)
udh.left(110)
udh.forward(46)
udh.end_fill()
go(-208,-55)
udh.fillcolor('#1E6649')
udh.begin_fill()
udh.right(55+180)
udh.forward(40)
udh.left(90+35)
udh.forward(36)
udh.left(110)
udh.forward(36)
udh.end_fill()
#tree 2
udh.right(55+180)
go(500,-200)
udh.fillcolor('#3F2A32')
udh.begin_fill()
udh.left(175)
udh.forward(60)
udh.right(85)
udh.forward(10)
udh.right(85)
udh.forward(60)
udh.right(95)
udh.forward(20)
udh.end_fill()
udh.right(180)
go(-218,-140)
udh.fillcolor('#1E6649')
udh.begin_fill()
udh.forward(60)
udh.left(90+35)
udh.forward(56)
udh.left(110)
udh.forward(56)
udh.end_fill()
go(-213,-94)
udh.fillcolor('#1E6649')
udh.begin_fill()
udh.right(55+180)
udh.forward(50)
udh.left(90+35)
udh.forward(46)
udh.left(110)
udh.forward(46)
udh.end_fill()
go(-208,-55)
udh.fillcolor('#1E6649')
udh.begin_fill()
udh.right(55+180)
udh.forward(40)
udh.left(90+35)
udh.forward(36)
udh.left(110)
udh.forward(36)
udh.end_fill()
print(udh.xcor(), " ",udh.ycor(), " ",)
turtle.done()