import turtle
wn = turtle.screen()
wn.title("ping pong")
wn.bgcolor("black")
wn.setup(width=800, heigh=600)
wn.tracer(0)

#första paddeln
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.spasize(stretch_wid=5, stetch_len=1)
paddle_a.penup()
paddle_agotol(-350, 0)
