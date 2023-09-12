from  turtle import Turtle
STARING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
class Snake:
   def __init__(self):
       self.segments=[]
       self.creatSnake()
       self.head=self.segments[0]
   def creatSnake(self):
       for position in STARING_POSITION:
           self.add_segment(position)
   def add_segment(self,position):
       new_segment = Turtle("square")
       new_segment.color("white")
       new_segment.penup()
       new_segment.goto(position)
       self.segments.append(new_segment)
   def extend(self):
       self.add_segment(self.segments [-1].position())
   def move(self):
        for seg_num in range(len(self.segments) - 1 ,0 ,-1 ):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y )
        self.segments[0].forward(MOVE_DISTANCE)
   def up(self):
       self.head.setheading(90)
   def down(self):
       self.head.setheading(270)

   def left(self):
       self.head.setheading(180)

   def right(self):
       self.head.setheading(0)

