from turtle import *

shape("turtle")
speed(1)
#we want to paint a house

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a windows
penup()
goto(50, 150)
pendown()

left(30)
color("brown")
begin_fill()
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)
end_fill()


penup()
goto(150, 150)
pendown()

begin_fill()
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)
end_fill()

exitonclick()