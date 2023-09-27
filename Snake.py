from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    segments = []

    def __init__(self, positions):
        self.positions = positions
        for position in self.positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        self.head = self.segments[-1]

    def move(self, wall=False):
        for i in range(len(self.segments) - 1):
            new_x = self.segments[i + 1].xcor()
            new_y = self.segments[i + 1].ycor()
            self.segments[i].goto(new_x, new_y)

        if not wall:
            if self.head.xcor() > 280:
                self.head.goto(-280, self.head.ycor())
            elif self.head.xcor() < -280:
                self.head.goto(280, self.head.ycor())
            elif self.head.ycor() > 280:
                self.head.goto(self.head.xcor(), -280)
            elif self.head.ycor() < -280:
                self.head.goto(self.head.xcor(), 280)
            else:
                self.head.forward(MOVE_DISTANCE)
        else:
            self.head.forward(MOVE_DISTANCE)

    def grow(self):
        new_x = self.segments[0].xcor()
        new_y = self.segments[0].ycor()
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(new_x, new_y)
        self.segments.insert(0, segment)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
