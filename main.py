import turtle

turtle.title("rainbow")
turtle.speed(100)
turtle.bgcolor("black")
r, g, b = 255, 0, 0

for i in range(255*5):
    turtle.colormode(255)
    if i < 255//3:
        g += 3
    elif i < 255*2//3:
        g -= 3
    elif i < 255:
        b += 3
    elif i < 255*4//3:
        g -= 3
    elif i < 255*5//3:
        r += 3
    else:
        b -= 3
    turtle.fd(50+i)
    turtle.rt(72)
    turtle.pencolor(r, g, b)
turtle.done()