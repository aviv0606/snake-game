from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.__segments = []
        self.head = None
        self.__create_snake()
        self.__direction = "RIGHT"  # 1-RIGHT, 2-LEFT, 3-UP, 4-DOWN

    def __create_snake(self):
        for p in POSITIONS:
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(p)
            self.__segments.append(segment)
        self.head = self.__segments[0]

    def move(self):
        for i in range(len(self.__segments) - 1, 0, -1):
            self.__segments[i].goto((self.__segments[i - 1].xcor(), self.__segments[i - 1].ycor()))
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.__direction == "RIGHT":
            self.head.left(90)
            self.__direction = "UP"
        elif self.__direction == "LEFT":
            self.head.right(90)
            self.__direction = "UP"

    def move_down(self):
        if self.__direction == "RIGHT":
            self.head.right(90)
            self.__direction = "DOWN"
        elif self.__direction == "LEFT":
            self.head.left(90)
            self.__direction = "DOWN"

    def move_left(self):
        if self.__direction == "UP":
            self.head.left(90)
            self.__direction = "LEFT"
        elif self.__direction == "DOWN":
            self.head.right(90)
            self.__direction = "LEFT"

    def move_right(self):
        if self.__direction == "UP":
            self.__segments[0].right(90)
            self.__direction = "RIGHT"
        elif self.__direction == "DOWN":
            self.__segments[0].left(90)
            self.__direction = "RIGHT"

    def extend_snake(self):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.__segments[-1].xcor(), self.__segments[-1].ycor())
        self.__segments.append(segment)

    def check_collision(self):
        for i in range(len(self.__segments) - 1, 0, -1):
            if self.head.distance(self.__segments[i].position()) < 10:
                return True
        return False
