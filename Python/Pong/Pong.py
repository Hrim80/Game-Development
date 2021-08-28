import turtle

wn = turtle.Screen()
wn.title("Pong by Hrishikesh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = 0.09


# Function
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)
    
def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)
    
def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)
    
def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)
    
# Keyboardbinding
wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")

# Gameloop
while True:
    wn.update()

    # Ball movement 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border Checking
    if ball.ycor()>=300:
        ball.sety(300)
        ball.dy *= -1

    if ball.ycor()<=-300:
        ball.sety(-300)
        ball.dy *= -1

    if ball.xcor()>=paddle_B.xcor():
        ball.setx(paddle_B.xcor())
        ball.dx *= -1

    if ball.xcor()<=-400:
        ball.setx(-400)
        ball.dx *= -1

    # if ball.xcor() > 390:
    #     ball.goto(0,0)
    #     ball.dx *= -1