import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        #ball bounce
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()



    #derect that r_paddle misses the ball
    # screen width h -> 800, paddle is at 350, yaani ki bw 340 - 360, to agr ball iske beyond gyi to mtlb ball miss krdi
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()