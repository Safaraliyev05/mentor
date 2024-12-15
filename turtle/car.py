import turtle


def draw_rectangle(color, x, y, width, height):
    """Draw a filled rectangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_circle(color, x, y, radius):
    """Draw a filled circle."""
    turtle.penup()
    turtle.goto(x, y - radius)  # Adjust position to draw circle from center
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_ferrari():
    """Draw a side view of a Ferrari-like car."""
    turtle.speed(3)

    # Draw the car body
    draw_rectangle("red", -150, 0, 300, 50)  # Main body
    draw_rectangle("red", -100, 50, 200, 40)  # Top cabin

    # Draw windows
    draw_rectangle("black", -90, 55, 80, 30)  # Front window
    draw_rectangle("black", 20, 55, 80, 30)  # Rear window

    # Draw wheels
    draw_circle("black", -100, -20, 30)  # Front wheel
    draw_circle("black", 100, -20, 30)  # Rear wheel
    draw_circle("gray", -100, -20, 15)  # Front hubcap
    draw_circle("gray", 100, -20, 15)  # Rear hubcap

    # Draw details
    turtle.penup()
    turtle.goto(-150, -10)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.forward(300)  # Bottom edge of the car


# Set up screen
screen = turtle.Screen()
screen.title("Ferrari Side View")
screen.bgcolor("lightblue")

# Draw the Ferrari
draw_ferrari()

# Finish
turtle.hideturtle()
screen.mainloop()
