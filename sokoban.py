import pyglet
import math
from pyglet import image
from pyglet.window import key

WIDTH = 1200
HEIGHT = 1000

size = 40
robko_x = WIDTH // size // 2 * size
robko_y = HEIGHT // size // 2 * size

robko_mx = 0
robko_my = 0

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

@window.event
def on_draw():
    window.clear()
    draw_square(robko_x,robko_y,size)

def draw_square(x, y, size, colour = (255,255,255,0)):
    img = image.create(size, size, image.SolidColorImagePattern(colour))
    img.blit(x,y)


def on_key_press(symbol,modifier):
    global robko_mx, robko_my
    if symbol == key.W:
        robko_mx = 0
        robko_my = size
    if symbol == key.S:
        robko_mx = 0
        robko_my = -size
    if symbol == key.A:
        robko_mx = -size
        robko_my = 0
    if symbol == key.D:
        robko_mx = size
        robko_my = 0
def on_key_release(symbol,modifier):
    global robko_mx, robko_my
    if symbol == key.W:
        robko_mx = 0
        robko_my = 0
    if symbol == key.S:
        robko_mx = 0
        robko_my = 0
    if symbol == key.A:
        robko_mx = 0
        robko_my = 0
    if symbol == key.D:
        robko_mx = 0
        robko_my = 0


def update(dt):
    global robko_x,robko_y
    robko_x += robko_mx
    robko_y += robko_my


pyglet.clock.schedule_interval(update,1/30)
window.push_handlers(
    on_key_press=on_key_press,
    on_key_release=on_key_release
)
pyglet.app.run()