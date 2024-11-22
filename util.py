import turtle

# 이동 중 자취를 남기지 않고 특정 좌표로 이동하는 함수
def set_pos(x, y):
    turtle.speed(0) #속도 설정
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# 국기의 테두리를 그리는 함수
def draw_border(w, h):
    set_pos(-w/2, h/2)
    turtle.color('black')
    turtle.seth(0)
    turtle.speed(3)
    for _ in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

# 원을 그리는 함수
def draw_circle(x, y, r, color):
    set_pos(x, y - r)
    turtle.seth(0)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

# 주어진 좌표들로 다각형을 그리는 함수
def draw_poly(coords, color):
    turtle.color(color)
    set_pos(coords[0][0], coords[0][1])
    turtle.begin_fill()
    for x, y in coords[1:]: 
        turtle.goto(x, y)
    turtle.goto(coords[0][0], coords[0][1])
    turtle.end_fill()

# 왼쪽 상단 좌표와 오른쪽 하단 좌표를 받아서 사각형을 그리는 함수
def draw_rect(x1, y1, x2, y2, color):
    set_pos(x1, y1)
    turtle.color(color)
    w, h = x2 - x1, y1 - y2
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)
    turtle.end_fill()

# 왼쪽 상단 좌표와 가로, 세로 길이를 받아서 사각형을 그리는 함수
def draw_rect_with_length(x, y, w, h, color):
    draw_rect(x, y, x + w, y - h, color)

# 별을 그리는 함수
def draw_star(x, y, r, color, angle=0):
    set_pos(x, y)
    turtle.color(color)
    turtle.seth(angle)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(r)
        turtle.right(144)
        turtle.forward(r)
        turtle.left(72)
    turtle.end_fill()
