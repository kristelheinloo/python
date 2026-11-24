# Kristel 11.11.26

#Rõngad
import turtle

## Aken
aken = turtle.Screen()
aken.setup(width=800, height=600)
aken.title("Kristel  - olümpiarõngad")
## Liigutan õigesse kohta
turtle.speed(0)
turtle.up()
turtle.goto(-150,50)
turtle.down()

## Ring 1
turtle.pensize(6)
turtle.pencolor("blue")
turtle.circle(50)

turtle.up()
turtle.goto(-40,50)
turtle.down()

## Ring 2
turtle.pensize(6)
turtle.pencolor("black")
turtle.circle(50)
## Ring 3
turtle.pensize(6)
turtle.pencolor("red")
turtle.circle(50)




turtle.done()