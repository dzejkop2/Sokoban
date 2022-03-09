import pyglet
from pyglet import image
from pyglet.window import key

WIDTH = 576
HEIGHT = 672
REFRESH_RATE = 1/15
FONTSIZE = 36

SKORE = [0]
max_skore = 4

level1 = False
level2 = True

#robko
size = 32


window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

#vykresluje kocky
@window.event
def on_draw():
    window.clear()
    background = image.load("tiles/level.png")
    background.blit(0,0)
    skore = pyglet.text.Label(f"{SKORE[0]} / {max_skore}", font_size=FONTSIZE, x=160, y= HEIGHT - 96, anchor_x="right")
    skore.draw()
    draw_square(robko_x, robko_y, size, (255, 255, 255, 0))
    draw_square(box1_x, box1_y, size, (255, 1, 1, 0))


    """
    draw_square(box_check_x, box_check_y, size, (1, 255, 1, 0))
    robo = image.load("robko.png")
    robo.blit(robko_x, robko_y)
    """

def check_box1(dt):
    global box1_x, box1_y
    print(robko_x, robko_y)
    if box1_x == box_check1_x:
        if box1_y == box_check1_y:
            SKORE[0] += 1
            pyglet.clock.unschedule(check_box1)
def check_box2(dt):
    global box2_x, box2_y
    if box2_x == box_check2_x:
        if box2_y == box_check2_y:
            SKORE[0] += 1
            pyglet.clock.unschedule(check_box2)
def check_box3(dt):
    global box3_x, box3_y
    if box3_x == box_check3_x:
        if box3_y == box_check3_y:
            SKORE[0] += 1
            pyglet.clock.unschedule(check_box3)
def check_box4(dt):
    global box4_x, box4_y
    if box4_x == box_check4_x:
        if box4_y == box_check4_y:
            SKORE[0] += 1
            pyglet.clock.unschedule(check_box4)
#zadáva ako vykresliť kocku
def draw_square(x, y, size, color):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x,y)

def block(block_x,block_y):
    image.load("tiles/stone.png")
    image.blit(block_x,block_y)


def box_barrier(dt):
    global robko_x,robko_y,box1_x,box1_y,box2_x,box2_y,box3_x,box3_y,box4_x,box4_y
    if box1_x == 416:
        if robko_x >= box1_x:
            if robko_y == box1_y:
                robko_x -= size
    elif box1_x == 128:
        if robko_x <= box1_x:
            if robko_y == box1_y:
                robko_x += size
    elif box1_y == 384:
        if robko_y >= box1_y:
            if robko_x == box1_x:
                robko_y -= size
    elif box1_y == 128:
        if robko_y <= box1_y:
            if robko_x == box1_x:
                robko_y += size
    if box2_x == 416:
        if robko_x >= box2_x:
            if robko_y == box2_y:
                robko_x -= size
    elif box2_x == 128:
        if robko_x <= box2_x:
            if robko_y == box2_y:
                robko_x += size
    elif box2_y == 384:
        if robko_y >= box2_y:
            if robko_x == box2_x:
                robko_y -= size
    elif box2_y == 128:
        if robko_y <= box2_y:
            if robko_x == box2_x:
                robko_y += size
    if box3_x == 416:
        if robko_x >= box3_x:
            if robko_y == box3_y:
                robko_x -= size
    elif box3_x == 128:
        if robko_x <= box3_x:
            if robko_y == box3_y:
                robko_x += size
    elif box3_y == 384:
        if robko_y >= box3_y:
            if robko_x == box3_x:
                robko_y -= size
    elif box3_y == 128:
        if robko_y <= box3_y:
            if robko_x == box3_x:
                robko_y += size
    if box4_x == 416:
        if robko_x >= box4_x:
            if robko_y == box4_y:
                robko_x -= size
    elif box4_x == 128:
        if robko_x <= box4_x:
            if robko_y == box4_y:
                robko_x += size
    elif box4_y == 384:
        if robko_y >= box4_y:
            if robko_x == box4_x:
                robko_y -= size
    elif box4_y == 128:
        if robko_y <= box4_y:
            if robko_x == box4_x:
                robko_y += size
#zadáva kde sa môže pohybovať
def barrier(dt):
    global robko_x, robko_y,box1_x,box1_y
    if robko_x >= 416:
        robko_x = 416
    if robko_x <= 128:
        robko_x = 128
    if robko_y >= 384:
        robko_y = 384
    if robko_y <= 128:
        robko_y = 128
    if box1_x >= 416:
        box1_x = 416
    if box1_x <= 128:
        box1_x = 128
    if box1_y >= 384:
        box1_y = 384
    if box1_y <= 128:
        box1_y = 128

def box_move_UP():
    global box1_y,box2_y,box3_y,box4_y
    if robko_x == box1_x:
        if robko_y == box1_y:
            box1_y += size
    if robko_x == box2_x:
        if robko_y == box2_y:
            box2_y += size
    if robko_x == box3_x:
        if robko_y == box3_y:
            box3_y += size
    if robko_x == box4_x:
        if robko_y == box4_y:
            box4_y += size
def box_move_LEFT():
    global box1_x,box2_x,box3_x,box4_x
    if robko_y == box1_y:
        if robko_x == box1_x:
            box1_x -= size
    if robko_y == box2_y:
        if robko_x == box2_x:
            box2_x -= size
    if robko_y == box3_y:
        if robko_x == box3_x:
            box3_x -= size
    if robko_y == box4_y:
        if robko_x == box4_x:
            box4_x -= size
def box_move_RIGHT():
    global box1_x,box2_x,box3_x,box4_x
    if robko_y == box1_y:
        if robko_x == box1_x:
            box1_x += size
    if robko_y == box2_y:
        if robko_x == box2_x:
            box2_x += size
    if robko_y == box3_y:
        if robko_x == box3_x:
            box3_x += size
    if robko_y == box4_y:
        if robko_x == box4_x:
            box4_x += size
def box_move_DOWN():
    global box1_y,box2_y,box3_y,box4_y
    if robko_x == box1_x:
        if robko_y == box1_y:
            box1_y -= size
    if robko_x == box2_x:
        if robko_y == box2_y:
            box2_y -= size
    if robko_x == box3_x:
        if robko_y == box3_y:
            box3_y -= size
    if robko_x == box4_x:
        if robko_y == box4_y:
            box4_y -= size

#movement
def on_key_press(symbol,modifier):
    global robko_x, robko_y
    if symbol == key.W:
        robko_y += size
        box_move_UP()
    if symbol == key.S:
        robko_y -= size
        box_move_DOWN()
    if symbol == key.A:
        robko_x -= size
        box_move_LEFT()
    if symbol == key.D:
        robko_x += size
        box_move_RIGHT()

def schedules():
    pyglet.clock.schedule_interval(check_box1, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box2, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box3, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box4, REFRESH_RATE)
    pyglet.clock.schedule_interval(barrier, REFRESH_RATE)
    pyglet.clock.schedule_interval(box_barrier, REFRESH_RATE)

if level1 == True:
    robko_x = 256
    robko_y = 224
    box1_x = 192
    box1_y = 192
    box2_x = 0
    box2_y = 0
    box3_x = 0
    box3_y = 0
    box4_x = 0
    box4_y = 0
    box_check1_x = 800
    box_check1_y = 800
    box_check2_x = 0
    box_check2_y = 0
    box_check3_x = 0
    box_check3_y = 0
    box_check4_x = 0
    box_check4_y = 0

if level2 == True:
    robko_x = 288
    robko_y = 288
    box1_x = 160
    box1_y = 160
    box2_x = 0
    box2_y = 0
    box3_x = 0
    box3_y = 0
    box4_x = 0
    box4_y = 0
    box_check1_x = 800
    box_check1_y = 800
    box_check2_x = 0
    box_check2_y = 0
    box_check3_x = 0
    box_check3_y = 0
    box_check4_x = 0
    box_check4_y = 0

schedules()
window.push_handlers(
    on_key_press=on_key_press
)

pyglet.app.run()