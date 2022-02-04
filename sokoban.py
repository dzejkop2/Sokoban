import pyglet
from pyglet import image

from pyglet.window import key

WIDTH = 1000
HEIGHT = 800

size = 20
robko_x = WIDTH // size // 2 * size
robko_y = HEIGHT // size // 2 * size

robko_mx = 0
robko_my = 0

pressed_keys = set()

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

@window.event
def on_draw():
    window.clear()
    draw_square(robko_x,robko_y,size)

def draw_square(x, y, size, colour = (255,255,255,0)):
    img = image.create(size, size, image.SolidColorImagePattern(colour))
    img.blit(x,y)


def on_key_press(symbol,modifier):
    if symbol == key.W:
        pressed_keys.add("UP")
    if symbol == key.S:
        pressed_keys.add("DOWN")

def on_key_release(symbol,modifier):
    if symbol == key.W:
        pressed_keys.discard("UP")
    if symbol == key.S:
        pressed_keys.discard("DOWN")

def move():
    global robko_mx, robko_my
    if ("UP") in pressed_keys:
        robko_mx = 0
        robko_my = size
    if ("DOWN") in pressed_keys:
        robko_mx = 0
        robko_my = -size


def update(dt):
    global robko_x,robko_y
    robko_x += robko_mx
    robko_y += robko_my


window.push_handlers(
    on_key_press=on_key_press,
    on_key_release=on_key_release
)
pyglet.clock.schedule_interval(update,1/30)
pyglet.app.run()