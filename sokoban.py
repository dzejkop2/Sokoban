import pyglet
from pyglet import image
from pyglet.window import key

WIDTH = 1200
HEIGHT = 800

size = 40
size_box = 40

robko_x = WIDTH // size // 2 * size
robko_y = HEIGHT // size // 2 * size

box1_x = 400
box1_y = 400

box1_mx = 0
box1_my = 0

robko_mx = 0
robko_my = 0

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

#vykresluje kocky
@window.event
def on_draw():
    window.clear()
    draw_square(robko_x,robko_y,size, (255,255,255,0) )
    draw_square(box1_x, box1_y, size_box,(255,1,1,0))

#zadáva ako vykresliť kocku
def draw_square(x, y, size, color):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x,y)

#zadáva kde sa môže pohybovať
def barrier(dt):
    global robko_mx, robko_my, box1_mx, box1_my
    if robko_x + size == WIDTH:
        robko_mx = 0
    if robko_x == 0:
        robko_mx = 0
    if robko_y + size == HEIGHT:
        robko_my = 0
    if robko_y == 0:
        robko_my = 0

#movement
def on_key_press(symbol,modifier):
    global robko_mx, robko_my,box1_mx,box1_my,move_box
    if symbol == key.W:
        robko_mx = 0
        robko_my = size
        if robko_x == box1_x:
            if robko_y + size == box1_y:
                box1_my = size_box
    if symbol == key.S:
        robko_mx = 0
        robko_my = -size
        if robko_x == box1_x:
            if robko_y - size == box1_y:
                box1_my = -size_box
    if symbol == key.A:
        robko_mx = -size
        robko_my = 0
        if robko_y == box1_y:
            if robko_x - size == box1_x:
                box1_mx = -size_box
    if symbol == key.D:
        robko_mx = size
        robko_my = 0
        if robko_y == box1_y:
            if robko_x + size == box1_x:
                box1_mx = size_box


def on_key_release(symbol,modifier):
    global robko_mx, robko_my,box1_mx,box1_my,move_box
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
        move_box = 0
        robko_mx = 0
        robko_my = 0
        box1_mx = 0
        box1_my = 0


def update(dt):
    global robko_x,robko_y,box1_x,box1_y,box1_mx,box1_my
    robko_x += robko_mx
    robko_y += robko_my
    box1_x += box1_mx
    box1_y += box1_my

pyglet.clock.schedule_interval(update, 1/15)
pyglet.clock.schedule_interval(barrier, 1/15)
window.push_handlers(
    on_key_press=on_key_press,
    on_key_release=on_key_release
)
pyglet.app.run()