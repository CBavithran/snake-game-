from turtle import Turtle

STARTING_POST = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    
    def create_snake(self):
        for post in STARTING_POST:
            self.new_segment(post)
    
    def new_segment(self, post):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(post)
        self.segment.append(new_segment) 
        
    def extend(self):
        self.new_segment(self.segment[-1].position())
        
    def move_snake(self):
        for seg_num in range(len(self.segment) -1, 0, -1):
            new_x = self.segment[seg_num -1 ].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)   
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)