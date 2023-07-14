from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head= self.segments[0]



    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(90)

    def snake_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def snake_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def snake_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)




    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
