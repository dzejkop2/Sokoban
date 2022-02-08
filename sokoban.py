import pyglet
import math
from pyglet import image
from pyglet.window import key

WIDTH = 1200
HEIGHT = 1000

size = 40
size_box = 40

robko_x = WIDTH // size // 2 * size
robko_y = HEIGHT // size // 2 * size

box_x = WIDTH // size_box // 3 * size_box
box_y = WIDTH // size_box // 3 * size_box

box_mx = 0
box_my = 0

robko_mx = 0
robko_my = 0

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

@window.event
def on_draw():
    window.clear()
    draw_square(robko_x,robko_y,size, (255,255,255,0))
    draw_square(box_x, box_y, size_box, (255,1,1,0))

def draw_square(x, y, size, colour):
    img = image.create(size, size, image.SolidColorImagePattern(colour))
    img.blit(x,y)

def on_key_press(symbol,modifier):
    global robko_mx, robko_my,box_mx,box_my
    if symbol == key.W:
        robko_mx = 0
        robko_my = size
        if robko_x == box_x:
            if robko_y + size == box_y:
                box_my = size_box
    if symbol == key.S:
        robko_mx = 0
        robko_my = -size
        if robko_x == box_x:
            if robko_y - size == box_y:
                box_my = -size_box
    if symbol == key.A:
        robko_mx = -size
        robko_my = 0
        if robko_y == box_y:
            if robko_x - size == box_x:
                box_mx = -size_box
    if symbol == key.D:
        robko_mx = size
        robko_my = 0
        if robko_y == box_y:
            if robko_x + size == box_x:
                box_mx = size_box
def on_key_release(symbol,modifier):
    global robko_mx, robko_my,box_mx,box_my
    if symbol == key.W:
        robko_mx = 0
        robko_my = 0
        box_mx = 0
        box_my = 0
    if symbol == key.S:
        robko_mx = 0
        robko_my = 0
        box_mx = 0
        box_my = 0
    if symbol == key.A:
        robko_mx = 0
        robko_my = 0
        box_mx = 0
        box_my = 0
    if symbol == key.D:
        robko_mx = 0
        robko_my = 0
        box_mx = 0
        box_my = 0


def update(dt):
    global robko_x,robko_y,box_x,box_y,box_mx,box_my
    robko_x += robko_mx
    robko_y += robko_my
    box_x += box_mx
    box_y += box_my

pyglet.clock.schedule_interval(update,1/15)
window.push_handlers(
    on_key_press=on_key_press,
    on_key_release=on_key_release
)
pyglet.app.run()