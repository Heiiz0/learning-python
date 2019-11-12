import turtle 
import random 

rosi = turtle.Turtle()
rosi.shape("turtle")
rosi.pensize(5)

def haus():
    rosi.pencolor(random.choice(("red","blue","green","purple","pink","yellow")))
    rosi.fillcolor(random.choice(("red","blue","green","purple","pink","yellow")))
    rosi.pensize(random.randint(1,20))
    rosi.begin_fill()
    rosi.forward(150)
    rosi.left(90)
    rosi.forward(100)
    rosi.left(45)
    rosi.forward(75)
    rosi.left(75)
    rosi.forward(100)
    rosi.left(60)
    rosi.forward(110)
    rosi.left(90)
    rosi.end_fill()
    
for a in range(101):
    rosi.penup()
    x = random.randint(-250,250)
    y = random.randint(-300,300)
    rosi.goto(x,y)
    rosi.pendown()
    rosi.setheading(0)    
    haus()
    


turtle.exitonclick()
