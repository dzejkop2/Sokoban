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
level2 = False
menu = True
barrier_x_max = 416
barrier_x_min = 128
barrier_y_max = 384
barrier_y_min = 128
robko_x = 0
robko_y = 0
box1_x = 0
box1_y = -1
box2_x = 0
box2_y = -2
box3_x = 0
box3_y = -3
box4_x = 0
box4_y = -4
box_check1_x = -1
box_check1_y = 0
box_check2_x = -2
box_check2_y = 0
box_check3_x = -3
box_check3_y = 0
box_check4_x = -4
box_check4_y = 0

box1 = image.load("tiles/box.png")
box2 = image.load("tiles/box.png")
box3 = image.load("tiles/box.png")
box4 = image.load("tiles/box.png")
lvl1 = image.load("tiles/level1_nahlad.png")
lvl2 = image.load("tiles/level2_nahlad.png")
checked_box = pyglet.image.load("tiles/box_checked.png")
vyber = pyglet.sprite.Sprite(lvl1)
vyber.x = -200
vyber.y = -200

pick_lvl1 = 0
pick_lvl2 = 0

size = 32

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
def check_lvl(dt):
    global robko_x,robko_y,box1_x,box1_y,box2_x,box2_y,box3_x,box3_y,box4_x,box4_y,box_check1_x,box_check1_y,box_check2_x,box_check2_y,box_check3_x,box_check3_y,box_check4_x,box_check4_y
    if level1 == True:
        robko_x = 256
        robko_y = 224
        box1_x = 224
        box1_y = 288
        box2_x = 224
        box2_y = 224
        box3_x = 320
        box3_y = 288
        box4_x = 320
        box4_y = 224
        box_check1_x = 128
        box_check1_y = 288
        box_check2_x = 224
        box_check2_y = 128
        box_check3_x = 416
        box_check3_y = 224
        box_check4_x = 320
        box_check4_y = 384
    elif level2 == True:
        robko_x = 256
        robko_y = 192
        box1_x = 128
        box1_y = 192
        box2_x = 224
        box2_y = 192
        box3_x = 320
        box3_y = 192
        box4_x = 416
        box4_y = 192
        box_check1_x = 224
        box_check1_y = 288
        box_check2_x = 128
        box_check2_y = 384
        box_check3_x = 320
        box_check3_y = 288
        box_check4_x = 416
        box_check4_y = 384

#vykresluje kocky
@window.event
def on_draw():
    if menu == True:
        background = image.load("tiles/menu.png")
        background.blit(0,0)
        vyber.draw()
    if menu == False:
        window.clear()
        if level1 == True:
            background = image.load("tiles/level1.png")
            background.blit(0, 0)
        elif level2 == True:
            background = image.load("tiles/level2.png")
            background.blit(0,0)
        skore = pyglet.text.Label(f"{SKORE[0]} / {max_skore}", font_size=FONTSIZE, x=160, y=HEIGHT - 96,
                                      anchor_x="right")
        skore.draw()
        draw_square(robko_x, robko_y, size, (255, 255, 255, 0))
        box1.blit(box1_x, box1_y)
        box2.blit(box2_x, box2_y)
        box3.blit(box3_x, box3_y)
        box4.blit(box4_x, box4_y)
        if max_skore == SKORE[0]:
            vyhra = pyglet.text.Label("Vyhral si!", font_size=32, x =370, y=288, anchor_x="right")
            vyhra.draw()

def draw_square(x, y, size, color):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x,y)


def check_box1(dt):
    global box1, box2, box3, box4
    print(robko_x, robko_y)
    if box1_x == box_check1_x:
        if box1_y == box_check1_y:
            SKORE[0] += 1
            box1 = checked_box
            pyglet.clock.unschedule(check_box1)
    elif box2_x == box_check1_x:
        if box2_y == box_check1_y:
            SKORE[0] += 1
            box2 = checked_box
            pyglet.clock.unschedule(check_box1)
    elif box3_x == box_check1_x:
        if box3_y == box_check1_y:
            SKORE[0] += 1
            box3 = checked_box
            pyglet.clock.unschedule(check_box1)
    elif box4_x == box_check1_x:
        if box4_y == box_check1_y:
            SKORE[0] += 1
            box4 = checked_box
            pyglet.clock.unschedule(check_box1)
def check_box2(dt):
    global box1,box2,box3,box4
    if box1_x == box_check2_x:
        if box1_y == box_check2_y:
            SKORE[0] += 1
            box1 = checked_box
            pyglet.clock.unschedule(check_box2)
    elif box2_x == box_check2_x:
        if box2_y == box_check2_y:
            SKORE[0] += 1
            box2 = checked_box
            pyglet.clock.unschedule(check_box2)
    elif box3_x == box_check2_x:
        if box3_y == box_check2_y:
            SKORE[0] += 1
            box3 = checked_box
            pyglet.clock.unschedule(check_box2)
    elif box4_x == box_check2_x:
        if box4_y == box_check2_y:
            SKORE[0] += 1
            box4 = checked_box
            pyglet.clock.unschedule(check_box2)
def check_box3(dt):
    global box1,box2,box3,box4
    if box1_x == box_check3_x:
        if box1_y == box_check3_y:
            SKORE[0] += 1
            box1 = checked_box
            pyglet.clock.unschedule(check_box3)
    elif box2_x == box_check3_x:
        if box2_y == box_check3_y:
            SKORE[0] += 1
            box2 = checked_box
            pyglet.clock.unschedule(check_box3)
    elif box3_x == box_check3_x:
        if box3_y == box_check3_y:
            SKORE[0] += 1
            box3 = checked_box
            pyglet.clock.unschedule(check_box3)
    elif box4_x == box_check3_x:
        if box4_y == box_check3_y:
            SKORE[0] += 1
            box4 = checked_box
            pyglet.clock.unschedule(check_box3)
def check_box4(dt):
    global box1, box2, box3, box4
    if box1_x == box_check4_x:
        if box1_y == box_check4_y:
            SKORE[0] += 1
            box1 = checked_box
            pyglet.clock.unschedule(check_box4)
    elif box2_x == box_check4_x:
        if box2_y == box_check4_y:
            SKORE[0] += 1
            box2 = checked_box
            pyglet.clock.unschedule(check_box4)
    elif box3_x == box_check4_x:
        if box3_y == box_check4_y:
            SKORE[0] += 1
            box3 = checked_box
            pyglet.clock.unschedule(check_box4)
    elif box4_x == box_check4_x:
        if box4_y == box_check4_y:
            SKORE[0] += 1
            box4 = checked_box
            pyglet.clock.unschedule(check_box4)

def box_barrier_lvl1(x,y):
    global robko_x,robko_y
    if x == barrier_x_max:
        if robko_x >= x:
            if robko_y == y:
                robko_x -= size
    elif x == barrier_x_min:
        if robko_x <= x:
            if robko_y == y:
                robko_x += size
    elif y == barrier_y_max:
        if robko_y >= y:
            if robko_x == x:
                robko_y -= size
    elif y == barrier_y_min:
        if robko_y <= y:
            if robko_x == x:
                robko_y += size
def box_barrier_lvl2(x,y):
    global robko_x, robko_y
    if x == barrier_x_max:
        if robko_x >= x:
            if robko_y == y:
                robko_x -= size
    elif x == barrier_x_min:
        if robko_x <= x:
            if robko_y == y:
                robko_x += size
    elif y == barrier_y_max:
        if robko_y >= y:
            if robko_x == x:
                robko_y -= size
    elif y == barrier_y_min:
        if robko_y <= y:
            if robko_x == x:
                robko_y += size
def box_barrier(dt):
    global robko_x,robko_y,box1_x,box1_y,box2_x,box2_y,box3_x,box3_y,box4_x,box4_y
    if level1 == True:
        box_barrier_lvl1(box1_x, box1_y)
        box_barrier_lvl1(box2_x, box2_y)
        box_barrier_lvl1(box3_x, box3_y)
        box_barrier_lvl1(box4_x, box4_y)
    if level2== True:
        box_barrier_lvl2(box1_x, box1_y)
        box_barrier_lvl2(box2_x, box2_y)
        box_barrier_lvl2(box3_x, box3_y)
        box_barrier_lvl2(box4_x, box4_y)

def barrier_lvl1(x,y):
    if x >= barrier_x_max:
        x = barrier_x_max
    if x <= barrier_x_min:
        x = barrier_x_min


def barrier(dt):
    global robko_x, robko_y,box1_x,box1_y,box2_x,box2_y,box3_x,box3_y,box4_x,box4_y
    if level1 == True:
        barrier_lvl1(robko_x, robko_y)
        barrier_lvl1(box1_x, box1_y)
        barrier_lvl1(box2_x, box2_y)
        barrier_lvl1(box3_x, box3_y)
        barrier_lvl1(box4_x, box4_y)
        """
        if box1_x >= 416:
            box1_x = 416
        if box1_x <= 128:
            box1_x = 128
        if box1_y >= 384:
            box1_y = 384
        if box1_y <= 128:
            box1_y = 128
        if box2_x >= 416:
            box2_x = 416
        if box2_x <= 128:
            box2_x = 128
        if box2_y >= 384:
            box2_y = 384
        if box2_y <= 128:
            box2_y = 128
        if box3_x >= 416:
            box3_x = 416
        if box3_x <= 128:
            box3_x = 128
        if box3_y >= 384:
            box3_y = 384
        if box3_y <= 128:
            box3_y = 128
        if box4_x >= 416:
            box4_x = 416
        if box4_x <= 128:
            box4_x = 128
        if box4_y >= 384:
            box4_y = 384
        if box4_y <= 128:
            box4_y = 128
        
        if box1_y == 320:
            if box1_x <= 192:
                box1_y = 288
        if box1_x == 192:
            if box1_y >= 320:
                box1_x = 224
        if box1_y == 192:
            if box1_x <= 192:
                box1_y = 224
        if box1_x == 192:
            if box1_y <= 192:
                box1_x = 224
        if box1_y == 320:
            if box1_x >= 352:
                box1_y = 288
        if box1_x == 352:
            if box1_y >= 320:
                box1_x = 320
        if box1_y == 192:
            if box1_x >= 352:
                box1_y = 224
        if box1_x == 352:
            if box1_y <= 192:
                box1_x = 320
        if box2_y == 320:
            if box2_x <= 192:
                box2_y = 288
        if box2_x == 192:
            if box2_y >= 320:
                box2_x = 224
        if box2_y == 192:
            if box2_x <= 192:
                box2_y = 224
        if box2_x == 192:
            if box2_y <= 192:
                box2_x = 224
        if box2_y == 320:
            if box2_x >= 352:
                box2_y = 288
        if box2_x == 352:
            if box2_y >= 320:
                box2_x = 320
        if box2_y == 192:
            if box2_x >= 352:
                box2_y = 224
        if box2_x == 352:
            if box2_y <= 192:
                box2_x = 320
        if box3_y == 320:
            if box3_x <= 192:
                box3_y = 288
        if box3_x == 192:
            if box3_y >= 320:
                box3_x = 224
        if box3_y == 192:
            if box3_x <= 192:
                box3_y = 224
        if box3_x == 192:
            if box3_y <= 192:
                box3_x = 224
        if box3_y == 320:
            if box3_x >= 352:
                box3_y = 288
        if box3_x == 352:
            if box3_y >= 320:
                box3_x = 320
        if box3_y == 192:
            if box3_x >= 352:
                box3_y = 224
        if box3_x == 352:
            if box3_y <= 192:
                box3_x = 320
        if box4_y == 320:
            if box4_x <= 192:
                box4_y = 288
        if box4_x == 192:
            if box4_y >= 320:
                box4_x = 224
        if box4_y == 192:
            if box4_x <= 192:
                box4_y = 224
        if box4_x == 192:
            if box4_y <= 192:
                box4_x = 224
        if box4_y == 320:
            if box4_x >= 352:
                box4_y = 288
        if box4_x == 352:
            if box4_y >= 320:
                box4_x = 320
        if box4_y == 192:
            if box4_x >= 352:
                box4_y = 224
        if box4_x == 352:
            if box4_y <= 192:
                box4_x = 320
        """
    if level2 == True:
        barrier_lvl1(robko_x, robko_y)
        """
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
        if box2_x >= 416:
            box2_x = 416
        if box2_x <= 128:
            box2_x = 128
        if box2_y >= 384:
            box2_y = 384
        if box2_y <= 128:
            box2_y = 128
        if box3_x >= 416:
            box3_x = 416
        if box3_x <= 128:
            box3_x = 128
        if box3_y >= 384:
            box3_y = 384
        if box3_y <= 128:
            box3_y = 128
        if box4_x >= 416:
            box4_x = 416
        if box4_x <= 128:
            box4_x = 128
        if box4_y >= 384:
            box4_y = 384
        if box4_y <= 128:
            box4_y = 128
        if robko_x == 288:
            if robko_y >= 216:
                robko_x += size
        if robko_x == 256:
            if robko_y >= 216:
                robko_x -= size
        if box1_x == 288:
            if box1_y >= 216:
                box1_x += size
        if box1_x == 256:
            if box1_y >= 216:
                box1_x -= size
        if box2_x == 288:
            if box2_y >= 216:
                box2_x += size
        if box2_x == 256:
            if box2_y >= 216:
                box2_x -= size
        if box3_x == 288:
            if box3_y >= 216:
                box3_x += size
        if box3_x == 256:
            if box3_y >= 216:
                box3_x -= size
        if box4_x == 288:
            if box4_y >= 216:
                box4_x += size
        if box4_x == 256:
            if box4_y >= 216:
                box4_x -= size
        """


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
def on_key_press(symbol,modifier):
    global robko_x, robko_y, level1, level2, menu, vyber_x, vyber_y
    if level1 == True or level2 == True:
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
    elif menu == True:
        global vyber
        if symbol == key.D:
            vyber.image = lvl2
            vyber.x = 318
            vyber.y = 190
        if symbol == key.A:
            vyber.image = lvl1
            vyber.x = 158
            vyber.y = 190
        if symbol == key.ENTER:
            if vyber.x == 318:
                level2 = True
                menu = False
                pyglet.clock.schedule_once(check_lvl, 0)
            elif vyber.x == 158:
                level1 = True
                menu = False
                pyglet.clock.schedule_once(check_lvl, 0)


def schedules():
    pyglet.clock.schedule_interval(check_box1, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box2, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box3, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box4, REFRESH_RATE)
    pyglet.clock.schedule_interval(barrier, REFRESH_RATE)
    pyglet.clock.schedule_interval(box_barrier, REFRESH_RATE)

schedules()
window.push_handlers(
    on_key_press=on_key_press
)

pyglet.app.run()