import turtle
import random

turtle.mode("logo")
num_turtles = 8
turtles = []
colors = ['Red', 'Yellow', 'Blue', 'Green', 'Magenta', 'Brown', 'Purple', 'Lime']
screen = turtle.Screen()
drawTurtle = turtle.Turtle()
drawTurtle.hideturtle()
drawTurtle.penup()
drawTurtle.speed(0)

def drawSquare(t, length):  #Draws a square of length "length" with turtle "t" where top right corner is turtles initial location
    drawTurtle.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.right(90)
    drawTurtle.end_fill()

def drawFinishLine():
    drawTurtle.goto(-375, 500)
    drawTurtle.right(90)

    drawTurtle.fillcolor("white")
    drawTurtle.begin_fill()
    for _ in range(2):
        drawTurtle.forward(750)
        drawTurtle.right(90)
        drawTurtle.forward(50)
        drawTurtle.right(90)
    drawTurtle.end_fill()
    drawTurtle.fillcolor("black")
    for _ in range(15):
        drawSquare(drawTurtle, 25)
        drawTurtle.forward(25)
        drawTurtle.right(90)
        drawTurtle.forward(25)
        drawTurtle.left(90)
        drawSquare(drawTurtle, 25)
        drawTurtle.forward(25)
        drawTurtle.left(90)
        drawTurtle.forward(25)
        drawTurtle.right(90)

def drawGround():
    drawTurtle.fillcolor("tan")
    drawTurtle.goto(-375, 450)
    drawTurtle.begin_fill()
    for _ in range(2):
        drawTurtle.forward(750)
        drawTurtle.right(90)
        drawTurtle.forward(950)
        drawTurtle.right(90)
    drawTurtle.end_fill()

    
def initializeTurtles():
    
    for i in range(num_turtles):
        #create turtle objects and set attributes
        turtles.append(turtle.Turtle())
        turtles[i].speed(10)
        turtles[i].shape("turtle")
        turtles[i].color(colors[i])
        #set turtle names
        setattr(turtles[i], "name", colors[i])
        setattr(turtles[i], "speeds", random.uniform(0, 2.5))
        #set starting positions
        turtles[i].penup()
        turtles[i].goto(-350 + (i) * 100, -400)
        turtles[i].pendown()
        turtles[i].pensize(3)

def raceTurtles():
    finished = False
    n = 1
    while not finished:
        for i in range(num_turtles):
            powerCheck(i, n)
            turtles[i].forward(turtles[i].speeds + random.uniform(0, 2.5))
            if checkEndCondition(i):
                finished = True
                winner = turtles[i].name
                updateTurtleWinners(winner)
                break
        n += 1
def checkEndCondition(i):
    if turtles[i].ycor() >= 475:
        return True
    return False
    
def updateTurtleWinners(winner):
    oldScores = []
    file = open("turtle_winners.txt", "r")
    for line in file:
        l = line.split()
        name = l[0]
        score = l[1]
        oldScores.append([name, score])
    file.close()
    file = open("turtle_winners.txt", "w")
    for entry in oldScores:
        if entry[0] == winner:
            entry[1] = int(entry[1]) + 1
        file.write(str(entry[0] + " " + str(entry[1]) + "\n"))
    file.close()

#Individual powers
def powerCheck(i, n):
    if i == 0:  #red turtle
        if n > 75:
            if random.randint(1, 50) == 1:
                #Find turtle in first place
                head = turtles[0]
                red = turtles[0]
                for turtle in turtles:
                    if turtle.ycor() >= head.ycor():
                        head = turtle
                if not head.name == "Red":
                    red.penup()
                    red.speed(5)
                    head.penup()
                    head.speed(5)

                    oldRedCoordinates = (red.xcor(), red.ycor())
                    red.goto(head.xcor(), head.ycor())
                    head.goto(oldRedCoordinates[0], oldRedCoordinates[1])

                    red.pendown()
                    red.speed(10)
                    head.pendown()
                    head.speed(10)

                    
def yellowPower():
    pass

def bluePower():
    pass

def greenPower():
    pass

def magentaPower():
    pass

def brownPower():
    pass

def purplePower():
    pass

def limePower():
    pass

def main():
    screen.screensize(1000, 1000)
    screen.bgcolor("light gray")

    drawFinishLine()
    drawGround()
    initializeTurtles()
    raceTurtles()

    screen.exitonclick()


#Run main
main()