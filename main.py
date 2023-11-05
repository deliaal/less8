import turtle

draw = turtle.Turtle()

#for i in range(4):
    #draw.forward(100)
    #draw.right(90)

#num_sides = 360
#side_leght = 1
#angle = 360.0 / num_sides

#for i in range(num_sides):
    #draw.forward(side_leght)
    #draw.right(angle)



#window = turtle.Screen()
#window.bgcolor("purple")
#window.title("My window for turtle")

#draw.color("pink")

#def shapefun(size, sides):
    #for i in range(sides):
        #draw.fd(size)
        #draw.right(360.0 / sides)
        #size = size + 5

#shapefun(150, 4)
#shapefun(170, 4)
#shapefun(190, 4)
#shapefun(210, 4)
#shapefun(230, 4)

#window2 = turtle.Screen()
#pen = turtle.Pen()
#colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink']
#window2.bgcolor('black')

#for i in range(360):
    #pen.pencolor(colors[i%7])
    #pen.width(i/100 + 1)
    #pen.forward(i)
    #pen.left(60)

window3 = turtle.Screen()
pen = turtle.Pen()
colors = ['red', 'pink']
window3.bgcolor('purple')
pen.penup()
pen.goto(-220, -25)
pen.pendown()


for i in range(1):
    pen.pencolor(colors[i % 2])
    pen.left(90)
    pen.forward(115)
    pen.right(90)
    pen.forward(20)

for i in range(9):
    pen.pencolor(colors[i % 2])
    pen.forward(20)
    pen.right(20)

for i in range(1):
    pen.pencolor(colors[i % 2])
    pen.forward(40)
    pen.left(180)

pen.penup()
pen.goto(-100, -25)
pen.pendown()

for i in range(1):
    pen.forward(40)
    pen.right(180)
    pen.penup()
    pen.goto(-100, -25)
    pen.pendown()
    pen.right(90)
    pen.forward(115)
    pen.right(90)
    pen.forward(40)
    pen.penup()
    pen.goto(-100, 30)
    pen.pendown()
    pen.forward(40)

pen.penup()
pen.goto(-20, -25)
pen.pendown()

for i in range(1):
    pen.forward(40)
    pen.right(180)
    pen.penup()
    pen.goto(-20, -25)
    pen.pendown()
    pen.right(90)
    pen.forward(115)


pen.penup()
pen.goto(60, -25)
pen.pendown()

for i in range(1):
     pen.forward(115)

pen.penup()
pen.goto(120, -25)
pen.pendown()

for i in range(1):
    pen.goto(160, 95)
    pen.goto(200, -25)
    pen.penup()
    pen.goto(135, 15)
    pen.pendown()
    pen.right(90)
    pen.forward(60)


turtle.done()
turtle.exitonclick()


