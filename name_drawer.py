"""
Module: name_drawer

9/11/24

A program to draw a name using one (or more) turtles.

Authors:
1) Sawyer Dentz - sdentz@sandiego.edu
2) Name - USD Email Address
"""


import turtle


#sets up screen and moves turtle to correct location
tr = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1200, height=900)
tr.pensize(5)
tr.penup()
tr.goto(-550, 100)


#This is the main function that activates the program when called
def main():
    color = str(input("Please input a color to use for the pen: "))
    print()
    name = str(input("Please input the name you would like to draw: "))
    print()

    drawWord(tr, color, name)

    screen.exitonclick()


#This function calls the letter functions depending on the given string
def drawWord(t: turtle, color: str, word: str):
    try:
        for letter in word:
            if letter == " ":
                letter = "Space"
            globals()["draw" + letter.upper()](t, color)
    except:
        print("The name or color inputted is invalid. Please only use letters and spaces.\nExiting...\n")
        exit()

#---------- These functions draw the individual letters ----------
#Each letter function moves the turtle to the correct spot and draws a single letter

#function to draw the letter "A"
def drawA(t: turtle, color: str):
    t.pencolor(color)
    t.right(90)
    t.forward(200)
    t.pendown()
    t.backward(200)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.penup()
    t.backward(100)
    t.left(90)
    t.pendown()
    t.backward(100)
    t.penup()
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.right(90)

#function to draw the letter "B"
def drawB(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(75)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(100)
    t.penup()
    t.backward(100)
    t.pendown()
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.backward(25)
    t.penup()
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.right(90)

#function to draw the letter "C"
def drawC(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(t.xcor() - 100, t.ycor() - 200)
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(100)
    t.pendown()
    t.left(90)
    t.forward(200)
    t.right(90)
    t.penup()
    t.forward(125)

#function to draw the letter "D"
def drawD(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(80)
    t.goto(t.xcor()+20, t.ycor() + 50)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.goto(t.xcor() - 20, t.ycor() + 50)
    t.backward(80)
    t.penup()
    t.forward(125)

#function to draw the letter "E"
def drawE(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(t.xcor()-100, t.ycor() - (200/2))
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(t.xcor()-100, t.ycor() - (200/2))
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(100)
    t.pendown()
    t.left(90)
    t.forward(200)
    t.penup()
    t.right(90)
    t.forward(125)

#function to draw the letter "F"
def drawF(t: turtle, color:str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(100)
    t.right(90)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.penup()
    t.backward(50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.penup()
    t.backward(200)
    t.left(90)
    t.forward(125)

#function to draw the letter "G"
def drawG(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.left(90)
    t.backward(50)
    t.penup()
    t.forward(50)
    t.right(90)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.forward(200)
    t.penup()
    t.right(90)
    t.forward(125)

#function to draw the letter "H"
def drawH(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.penup()
    t.goto(t.xcor() + 100, t.ycor() + 200)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.penup()
    t.goto(t.xcor() - 100, t.ycor() + 100)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(t.xcor() + 25, t.ycor() + 100)

#function to draw the letter "I"
def drawI(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(50)
    t.right(90)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.backward(50)
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(50)
    t.penup()
    t.goto(t.xcor() + 25, t.ycor() + 200)

#function to draw the letter "J"
def drawJ(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(50)
    t.right(90)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.backward(50)
    t.penup()
    t.goto(t.xcor() + 125, t.ycor() + 200)

#funciton to draw the letter "K"
def drawK(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.goto(t.xcor() + 100, t.ycor() + 100)
    t.penup()
    t.goto(t.xcor() - 100, t.ycor() - 200)
    t.pendown()
    t.left(180)
    t.forward(100)
    t.goto(t.xcor() + 100, t.ycor() - 100)
    t.penup()
    t.forward(200)
    t.right(90)
    t.forward(25)

#function to draw the letter "l"
def drawL(t: turtle, color: str):
    t.color(color)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.penup()
    t.goto(t.xcor() + 25, t.ycor() + 200)

#function to draw the letter "M"
def drawM(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.penup()
    t.backward(200)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.penup()
    t.backward(200)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.penup()
    t.backward(200)
    t.left(90)
    t.forward(25)

#function to draw the letter "N"
def drawN(t: turtle, color: str):
    t.color(color)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.penup()
    t.backward(200)
    t.pendown()
    t.goto(t.xcor() + 100, t.ycor() - 200)
    t.backward(200)
    t.penup()
    t.left(90)
    t.forward(25)

#function to draw the letter "O"
def drawO(t: turtle, color: str):
    t.color(color)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.penup()
    t.forward(125)

#function to draw the letter "P"
def drawP(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.penup()
    t.backward(100)
    t.pendown()
    t.backward(100)
    t.penup()
    t.forward(200)
    t.right(90)
    t.forward(125)

#function to draw the letter "Q"
def drawQ(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(90)
    t.right(90)
    t.forward(190)
    t.left(90)
    t.backward(90)
    t.left(90)
    t.forward(190)
    t.penup()
    t.goto(t.xcor() + 80, t.ycor() + - 180)
    t.pendown()
    t.goto(t.xcor() + 20, t.ycor() - 20)
    t.penup()
    t.goto(t.xcor() + 25, t.ycor() + 200)
    t.right(90)

#function to draw the letter "R"
def drawR(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(100)
    t.right(90)
    t.backward(100)
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(100)
    t.pendown()
    t.goto(t.xcor() + 100, t.ycor() - 100)
    t.penup()
    t.left(90)
    t.forward(25)
    t.goto(t.xcor(), t.ycor() + 200)

#function to draw the letter "S"   
def drawS(t: turtle, color: str):
    t.pencolor(color)
    t.forward(100)
    t.pendown()
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(100)
    t.penup()
    t.forward(125)
    t.left(90)
    t.forward(200)
    t.right(90)

#function to draw the letter "T"
def drawT(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.penup()
    t.backward(50)
    t.pendown()
    t.goto(t.xcor(), t.ycor() - 200)
    t.penup()
    t.goto(t.xcor() + 75, t.ycor() + 200)

#function to draw the letter "U"
def drawU(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.penup()
    t.right(90)
    t.forward(25)

#function to draw the letter "V"
def drawV(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.goto(t.xcor() + 50, t.ycor() - 200)
    t.goto(t.xcor() + 50, t.ycor() + 200)
    t.penup()
    t.forward(25)

#function to draw the letter "W"
def drawW(t: turtle, color: str):
    t.pencolor(color)
    t.right(90)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.penup()
    t.backward(200)
    t.right(90)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.penup()
    t.right(90)
    t.forward(25)

#function to draw the letter "X"
def drawX(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.goto(t.xcor() + 100, t.ycor() - 200)
    t.penup()
    t.backward(100)
    t.pendown()
    t.goto(t.xcor() + 100, t.ycor() + 200)
    t.penup()
    t.forward(25)

#function to draw the letter "Y"
def drawY(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.penup()
    t.backward(100)
    t.pendown()
    t.backward(100)
    t.right(90)
    t.backward(100)
    t.penup()
    t.forward(125)
    t.left(90)
    t.forward(200)
    t.right(90)

#function to draw the letter "Z"
def drawZ(t: turtle, color: str):
    t.pencolor(color)
    t.pendown()
    t.forward(100)
    t.goto(t.xcor() - 100, t.ycor() - 200)
    t.forward(100)
    t.penup()
    t.goto(t.xcor() + 25, t.ycor() + 200)

#function to draw a single space the size of one letter
def drawSPACE(t: turtle, color: str):
    t.goto(t.xcor() + 125, t.ycor())


main() #main function call to start the program and ask user for input