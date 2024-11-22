import turtle
import util
import math

def draw_korea():
    # 태극 문양
    util.set_pos(-100, 0)
    turtle.setheading(270)
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.right(180)
    turtle.circle(50, -180)
    turtle.circle(100, 180)
    turtle.end_fill()

    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.right(180)
    turtle.circle(50, -180)
    turtle.circle(100, -180)
    turtle.end_fill()

    # 건곤감리
    util.draw_poly([(-207, 74), (-153, 157), (-141, 149), (-195, 66)], 'black')
    util.draw_poly([(-186, 60), (-132, 144), (-120, 136), (-174, 53)], 'black')
    util.draw_poly([(-165, 46), (-111, 131), (-99, 123), (-153, 40)], 'black')

    util.draw_poly([(-207, -74), (-153, -157), (-141, -149), (-195, -66)], 'black')
    util.draw_poly([(-186, -60), (-161, -99), (-150, -92), (-174, -53)], 'black')
    util.draw_poly([(-153, -112), (-130, -147), (-118, -140), (-141, -103)], 'black')
    util.draw_poly([(-165, -46), (-111, -131), (-99, -123), (-153, -40)], 'black')

    util.draw_poly([(102, 124), (124, 87), (135, 94), (112, 130)], 'black')
    util.draw_poly([(131, 75), (154, 39), (166, 47), (143, 82)], 'black')
    util.draw_poly([(120, 136), (174, 52), (186, 61), (132, 143)], 'black')
    util.draw_poly([(141, 149), (164, 113), (176, 121), (153, 156)], 'black')
    util.draw_poly([(172, 101), (195, 65), (207, 72), (184, 108)], 'black')

    util.draw_poly([(153, -41), (165, -49), (142, -85), (130, -77)], 'black')
    util.draw_poly([(122, -88), (134, -97), (112, -132), (99, -124)], 'black')
    util.draw_poly([(174, -54), (186, -63), (164, -98), (151, -90)], 'black')
    util.draw_poly([(143, -102), (155, -110), (133, -145), (120, -137)], 'black')
    util.draw_poly([(195, -66), (207, -74), (185, -109), (172, -101)], 'black')
    util.draw_poly([(164, -116), (176, -124), (154, -159), (141, -151)], 'black')

    util.draw_border(600, 400)

def draw_america():  
    # 7개의 빨간색 줄
    for i in range(7):
        util.draw_rect(-380, 200-2*i*400/13, 380, 200-(2*i+1)*400/13, 'red') 
    
    # 왼쪽위 파란색 사각형 영역
    util.draw_rect(-380, 200, -80, 200-7*400/13, 'blue')
    
    # 별 그리기
    for i in range(9):
        y = 180 - 21*i
        if i % 2 == 0:
            for j in range(6):
                util.draw_star(-355 + 50*j, y, 8, 'white')
        else:
            for j in range(5):
                util.draw_star(-330 + 50*j, y, 8, 'white')

    util.draw_border(760, 400)

def draw_greece():  
    # 5개의 파란색 줄
    for i in range(5):
        util.draw_rect(-300, 200-2*i*400/9, 300, 200-(2*i+1)*400/9, 'royalblue') 
    
    # 왼쪽 위 문양
    length = 400/9*2
    util.draw_rect_with_length(-300, 200, length*5/2, length*5/2, 'white')
    util.draw_rect_with_length(-300, 200, length, length, 'royalblue')
    util.draw_rect_with_length(-300, 200-length*3/2, length, length, 'royalblue')
    util.draw_rect_with_length(-300+length*3/2, 200-length*3/2, length, length, 'royalblue')
    util.draw_rect_with_length(-300+length*3/2, 200, length, length, 'royalblue')

    util.draw_border(600, 400)

def draw_thailand():
    # 태국 국기가 6개의 줄로 이루어져 있다고 가정
    colors = ['red', 'white', 'navy', 'navy', 'white', 'red']

    # 6개의 줄을 그림
    for i in range(6):
        # 흰색은 안그려도 됨
        if colors[i] == 'white':
            continue
        util.draw_rect(-300, 200-i*400/6, 300, 200-(i+1)*400/6, colors[i])

    util.draw_border(600, 400)

def draw_united_kingdom():
    # 파랑색 영역 (배경으로 미리 그려놓음)
    util.draw_rect(-400, 200, 400, -200, 'navy')

    # 대각선 흰색 줄
    util.draw_poly([(-400, 200), (-400, 150), (320, -200), (400, -200), (400, -150), (-320, 200)], 'white')
    util.draw_poly([(-400, -200), (-400, -150), (320, 200), (400, 200), (400, 150), (-320, -200)], 'white')

    # 대각선 빨간색 줄
    util.draw_poly([(-400, 200), (-400, 170), (-400 + 300, 170 - 150), (-400 + 300, 200 - 150)], 'red')
    util.draw_poly([(400, -200), (400, -170), (400 - 300, -170 + 150), (400 - 300, -200 + 150)], 'red')
    

    util.draw_poly([(-400, -200), (-350, -200), (-350 + 300, -200 + 150), (-400 + 300, -200 + 150)], 'red')
    util.draw_poly([(400, 200), (350, 200), (350 - 300, 200 - 150), (400 - 300, 200 - 150)], 'red')

    # 흰색 십자가
    util.draw_rect(-400, 60, 400, -60, 'white')
    util.draw_rect(-60, 200, 60, -200, 'white')

    # 빨간색 십자가
    util.draw_rect(-400, 35, 400, -35, 'red')
    util.draw_rect(-35, 200, 35, -200, 'red')

    util.draw_border(800, 400)

def draw_china():
    # 빨간 배경
    util.draw_rect(-300, 200, 300, -200, 'red')

    # 커다란 별
    util.draw_star(-170, 100, 50, 'yellow')

    # 작은 별
    for i in range(4):
        x, y = -130, 70
        util.draw_star(x + math.cos(0.6*i - 0.9) * 100, 
                       y + math.sin(0.6*i - 0.9) * 100, 
                       15, 'yellow', 0.6*i * 180 / math.pi + 40)

    util.draw_border(600, 400)

def draw_south_sudan():
    # 3개의 선
    util.draw_rect(-400, 200, 400, 80, 'black')
    util.draw_rect(-400, 60, 400, -60, 'red')
    util.draw_rect(-400, -80, 400, -200, 'green')

    # 삼각형
    util.draw_poly([(-400, 200), (-400, -200), (-50, 0)], 'skyblue')

    # 별
    util.draw_star(-260, 20, 50, 'yellow')

    util.draw_border(800, 400)

def draw_india():
    # 3개의 선
    util.draw_rect(-300, 200, 300, 67, 'darkorange')
    util.draw_rect(-300, -200, 300, -67, 'green')

    # 가운데 문양
    n = 24 # 24등분 되어있음
    util.draw_circle(0, 0, 60, 'darkblue')
    util.draw_circle(0, 0, 50, 'white')
    util.draw_circle(0, 0, 13, 'darkblue')

    for i in range(n):
        theta = math.pi*2*i/n + math.pi/n
        x = 50 * math.cos(theta)
        y = 50 * math.sin(theta)
        util.draw_circle(x, y, 3, 'darkblue')

    util.set_pos(0, 0)
    for i in range(n):
        theta = math.pi*2*i/n + math.pi/n
        theta = theta*180/math.pi # 도 단위로 변환
        turtle.seth(theta - 3)
        turtle.begin_fill()
        turtle.forward(25)
        turtle.right(6)
        turtle.forward(25)
        turtle.right(174)
        turtle.forward(25)
        turtle.right(6)
        turtle.forward(25)
        turtle.end_fill()

    util.draw_border(600, 400)

def draw_switzerland():
    # 빨간 배경
    util.draw_rect(-200, 200, 200, -200, 'red')

    # 가운데 십자가
    util.draw_poly([(-40, 120),
                    (40, 120),
                    (40, 40),
                    (120, 40),
                    (120, -40),
                    (40, -40),
                    (40, -120),
                    (-40, -120),
                    (-40, -40),
                    (-120, -40),
                    (-120, 40),
                    (-40, 40)], 'white')

    util.draw_border(400, 400)

def draw_catarrh():
    # 자색 부분
    coords = [] # 자색 도형을 그리기 위한 좌표
    for i in range(19):
        x = -150 if i % 2 == 0 else -80
        y = 165 - 330/18*i
        coords.append((x, y))
    coords.append((420, -165))
    coords.append((420, 165))
    util.draw_poly(coords, 'maroon')

    util.draw_border(840, 330)

def draw_custom(): #나만의 국기 그리기
    util.draw_circle(-250, 0, 130, "salmon")
    util.draw_rect(-380, 200, -300, -200, "white") # 왼쪽에 삐져나온 부분을 가림
    util.draw_circle(250, 0, 130, "salmon")
    util.draw_rect(300, 200, 380, -200, "white") # 오른쪽에 삐져나온 부분을 가림
    util.draw_circle(-125, 0, 130, "orangered")
    util.draw_circle(125, 0, 130, "orangered")
    util.draw_circle(0, 0, 130, "red")
    util.draw_circle(0, 0, 50, "white")
    
    util.draw_border(600, 400)

flag_info = [
    {
        "name": "대한민국",
        "draw": draw_korea
    },
    {
        "name": "미국",
        "draw": draw_america
    },
    {
        "name": "그리스",
        "draw": draw_greece
    },
    {
        "name": "태국",
        "draw": draw_thailand
    },
    {
        "name": "영국",
        "draw": draw_united_kingdom
    },
    {
        "name": "중국",
        "draw": draw_china
    },
    {
        "name": "남수단",
        "draw": draw_south_sudan
    },
    {
        "name": "인도",
        "draw": draw_india
    },
    {
        "name": "스위스",
        "draw": draw_switzerland
    },
    {
        "name": "카타르",
        "draw": draw_catarrh
    },
    {
        "name": "철훈국",
        "draw": draw_custom
}]
