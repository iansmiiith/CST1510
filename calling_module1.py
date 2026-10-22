import turtle
#initialising the turtle
t = turtle.Turtle()
mycolors = ['red', 'green', 'blue', 'yellow', 'purple']
#radius for smallest circle
r = 10
#number of circles
n = 7
#loop for printing various colored circles
for i in range(n + 1,0,-1):
    t.color('black', mycolors[i%5])
    t.begin_fill()
    t.circle(r * i)
    t.end_fill()