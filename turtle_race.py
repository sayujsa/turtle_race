import random
import sys
from turtle import Turtle, Screen


def move_turtle(turtle_object):   # Move turtle a random distance
    spaces = [20, 12, 14, 18, 9, 3, 8]
    turtle_object.fd(random.choice(spaces))


# Set turtle to the starting position, also takes in y coordinate to set each one a bit above the one below
def set_pos(turtle_object, y_pos):
    turtle_object.goto(x=-280, y=y_pos)


screen = Screen()
screen.setup(600, 400)
try:
    guess = screen.textinput("Turtle Race", "Guess who will win : red/blue/orange/green/purple").lower()
except AttributeError:
    sys.exit(0)  # In case the user presses 'cancel', 'cancel' button returns a None type :(


turtle_red = Turtle("turtle")
turtle_blue = Turtle("turtle")
turtle_orange = Turtle("turtle")
turtle_green = Turtle("turtle")
turtle_purple = Turtle("turtle")

turtles = [turtle_red, turtle_blue, turtle_orange, turtle_green, turtle_purple]
colours = ["red", "blue", "orange", "green", "purple"]

i = 0
for y in range(-100, 61, 40):  # Assigning each turtle its colour
    turtles[i].penup()
    set_pos(turtles[i], y)
    turtles[i].color(colours[i])
    turtles[i].speed(1)
    i += 1

winning_turtle = ""


while True:
    for turtle_boi in turtles:   # Moving each turtle
        move_turtle(turtle_boi)

    if turtle_red.xcor() >= 280:   # Checking for the turtle who crosses the end first
        print("Red is the winner!")
        winning_turtle = "red"
        break
    elif turtle_blue.xcor() >= 280:
        print("Blue is the winner!")
        winning_turtle = "blue"
        break
    elif turtle_green.xcor() >= 280:
        print("Green is the winner!")
        winning_turtle = "green"
        break
    elif turtle_purple.xcor() >= 280:
        print("Purple is the winner!")
        winning_turtle = "purple"
        break
    elif turtle_orange.xcor() >= 280:
        print("Orange is the winner!")
        winning_turtle = "orange"
        break

if winning_turtle == guess:
    print("Your guess was correct!")
else:
    print("Your guess was wrong!")

screen.exitonclick()
