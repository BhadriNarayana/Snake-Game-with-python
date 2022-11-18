from turtle import Turtle

INITIAL_POSITIONS = [(0,0),(-20, 0),(-40, 0)]

class Snake:
    def __init__(self):
        self.turtle_collection = []
        for i in INITIAL_POSITIONS:
            self.add_length(i)
        self.turtle_collection[0].color("white")
        self.turtle_collection[0].shape("arrow")


    def add_length(self,pos):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(pos)
        self.turtle_collection.append(turtle)



    def move(self):

        for seg_num in range(len(self.turtle_collection) - 1, 0, -1):  # 3 -> 2 , 2-> 1
            new_x = self.turtle_collection[seg_num - 1].xcor()
            new_y = self.turtle_collection[seg_num - 1].ycor()
            self.turtle_collection[seg_num].goto(new_x, new_y)

        self.turtle_collection[0].forward(10)

    def l(self):
        if self.turtle_collection[0].heading() != 0:
            self.turtle_collection[0].setheading(180)

    def r(self):
        if self.turtle_collection[0].heading() != 180:
            self.turtle_collection[0].setheading(0)

    def d(self):
        if self.turtle_collection[0].heading() != 90:
            self.turtle_collection[0].setheading(270)

    def u(self):
        if self.turtle_collection[0].heading() != 270:
            self.turtle_collection[0].setheading(90)
