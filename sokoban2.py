import pyglet
from pyglet import image
from pyglet.window import key

WIDTH = 1200
HEIGHT = 800
REFRESH_RATE = 1/15
FONTSIZE = 36

SKORE = [0]
max_skore = 1

#robko
size = 40
robko_x = WIDTH // size // 2 * size
robko_y = HEIGHT // size // 2 * size
robko_mx = 0
robko_my = 0

#box 1
box1_x = 400
box1_y = 600
box1_mx = 0
box1_my = 0

box_check_x = 200
box_check_y = 200

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

#vykresluje kocky
@window.event
def on_draw():
    window.clear()
    draw_square(0, 0, 1500, (0, 191, 255, 0))
    text = pyglet.text.Label(str(SKORE[0]), font_size=FONTSIZE, x=100, y=HEIGHT - 100, anchor_x="right")
    text.draw()
    medzi = pyglet.text.Label("/", font_size=FONTSIZE, x=100 + FONTSIZE, y=HEIGHT - 100, anchor_x="right")
    medzi.draw()
    skore = pyglet.text.Label(str(max_skore), font_size=FONTSIZE, x= 100 + FONTSIZE * 2, y=HEIGHT - 100, anchor_x="right")
    skore.draw()
    draw_square(box_check_x, box_check_y, size, (1, 255, 1, 0))
    draw_square(box1_x, box1_y, size,(255, 1, 1, 0))
    draw_square(robko_x, robko_y, size, (255, 255, 255, 0))
    """
    robo = image.load("robko.png")
    robo.blit(robko_x, robko_y)
    """

def check_box1(dt):
    global box1_x, box1_y
    if box1_x == box_check_x:
        if box1_y == box_check_y:
            SKORE[0] += 1
            pyglet.clock.unschedule(check_box1)


#zadáva ako vykresliť kocku
def draw_square(x, y, size, color):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x,y)

#zadáva kde sa môže pohybovať
def barrier(dt):
    global robko_x, robko_y
    if robko_x >= WIDTH:
        robko_x = WIDTH - size
    if robko_x <= 0:
        robko_x = 0
    if robko_y >= HEIGHT:
        robko_y = HEIGHT - size
    if robko_y <= 0:
        robko_y = 0

def box_move_UP():
    global box1_y
    if robko_x == box1_x:
        if robko_y == box1_y:
            box1_y += size
def box_move_LEFT():
    global box1_x
    if robko_y == box1_y:
        if robko_x == box1_x:
            box1_x -= size
def box_move_RIGHT():
    global box1_x
    if robko_y == box1_y:
        if robko_x == box1_x:
            box1_x += size
def box_move_DOWN():
    global box1_y
    if robko_x == box1_x:
        if robko_y == box1_y:
            box1_y -= size

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

def on_key_release(symbol,modifier):
    global robko_mx, robko_my,box1_mx,box1_my
    if symbol == key.W:
        robko_mx = 0
        robko_my = 0
        box1_mx = 0
        box1_my = 0
    if symbol == key.S:
        robko_mx = 0
        robko_my = 0
        box1_mx = 0
        box1_my = 0
    if symbol == key.A:
        robko_mx = 0
        robko_my = 0
        box1_mx = 0
        box1_my = 0
    if symbol == key.D:
        robko_mx = 0
        robko_my = 0
        box1_mx = 0
        box1_my = 0

def schedules():
    # pyglet.clock.schedule_interval(check_box, REFRESH_RATE)
    pyglet.clock.schedule_interval(check_box1, REFRESH_RATE)
    # pyglet.clock.schedule_interval(update, REFRESH_RATE)
    pyglet.clock.schedule_interval(barrier, REFRESH_RATE)

schedules()
window.push_handlers(
    on_key_press=on_key_press,
    on_key_release=on_key_release
)
pyglet.app.run()