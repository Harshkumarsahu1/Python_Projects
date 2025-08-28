from turtle import Turtle, Screen
import random
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
t = Turtle()
s = Screen()
noofsides = 3
def set_sides(noofsides):
    t.color(random.choice(colors))
    angle = 360 / noofsides
    for _ in range(noofsides):
        t.forward(100)
        t.right(angle)

for sides in range(3, 11):
    set_sides(sides)    

s.exitonclick()