from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)  # 10/10 circle
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move #jo bhi x coor tha usme xmove add krdiya to go up
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # y ki jo bhi +, - value ho isse vo bounce hoke opp disha me aa jayega
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()