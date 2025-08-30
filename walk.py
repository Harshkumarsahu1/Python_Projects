import random
from turtle import Turtle, Screen
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
walk = [0, 90, 180, 270]
t = Turtle()
s = Screen()
for _ in range(200):
    t.color(random.choice(colors))
    t.left(random.choice(walk))
    t.forward(20)

s.exitonclick()