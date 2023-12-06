import turtle
import random

def draw_branch(turtle, branch_length, angle, width):
    if branch_length < 6:
        return
    else:
        turtle.pensize(width)
        if width <= 8:
            turtle.pencolor('green')
        else:
            turtle.pencolor('brown')
            
        turtle.forward(branch_length)
        new_length = branch_length * (random.uniform(0.7, 0.8))
        turtle.left(angle)
        draw_branch(turtle, new_length, angle, max(width - 1, 1))
        turtle.right(angle * 2)
        draw_branch(turtle, new_length, angle, max(width - 1, 1))
        turtle.left(angle)
        turtle.backward(branch_length)  

def draw_fractal_tree():
    screen = turtle.Screen()
    screen.bgcolor("white")
    my_turtle = turtle.Turtle()
    my_turtle.speed("fastest")
    my_turtle.color("brown")

    # 트리 시작 위치 설정
    my_turtle.penup()
    my_turtle.hideturtle()
    my_turtle.goto(0, -200)
    my_turtle.pendown()
    my_turtle.setheading(90)

    # 트리 그리기 시작
    initial_length = 100
    angle = 30
    draw_branch(my_turtle, initial_length, angle, 10)
    draw_branch(my_turtle, initial_length-30, angle, 10)
    screen.exitonclick()

draw_fractal_tree()
