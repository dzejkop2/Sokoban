import pyglet
import random

from pyglet.window import key
from pyglet import gl

WIDTH = 1000
HEIGHT = 800

SPEED = 200

rychlost_robka = [0,0]
VELKOST_ROBKA = 20
pozicia_robka = [WIDTH // 2, HEIGHT // 2]

klavesy = set()

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

"""
def text(text, x, y):
    text = pyglet.text.Label(text,font_size=36,x=x,y=y,anchor_x="center")
    text.draw()

def draw():
    text("Sokoban :)", x=WIDTH /2, y=HEIGHT/2)
"""

def square(x1,y1,x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()

def reset():
    pozicia_robka[0] = WIDTH // 2
    pozicia_robka[1] = HEIGHT // 2

    if random.randint(0, 1):
        rychlost_robka[0] = SPEED
    else:
        rychlost_robka[0] = -SPEED

    rychlost_robka[1] = random.uniform(-1, 1) * SPEED

def hrac():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)
    square(
        pozicia_robka[0] - VELKOST_ROBKA // 2,
        pozicia_robka[1] - VELKOST_ROBKA // 2,
        pozicia_robka[0] + VELKOST_ROBKA // 2,
        pozicia_robka[1] + VELKOST_ROBKA // 2
    )


#pridava stlacene klavesi
def key_press(symbol,modifier):
    if symbol == key.UP:
        klavesy.add('UP')
    if symbol == key.DOWN:
        klavesy.add('DOWN')
    if symbol == key.LEFT:
        klavesy.add('LEFT')
    if symbol == key.RIGHT:
        klavesy.add('RIGHT')

#odobera pustene klavesi
def key_release(symbol,modifier):
    if symbol == key.UP:
        klavesy.discard('UP')
    if symbol == key.DOWN:
        klavesy.discard('DOWN')
    if symbol == key.LEFT:
        klavesy.discard('LEFT')
    if symbol == key.RIGHT:
        klavesy.discard('RIGHT')

def posuvanie(dt):
    if ('UP') in klavesy:
        pozicia_robka[0] += rychlost_robka * dt
    if ('DOWN') in klavesy:
        pozicia_robka[1] -= rychlost_robka * dt


reset()
window.push_handlers(
    on_draw=hrac,
    on_key_press=key_press,
    on_key_release=key_release
)

pyglet.clock.schedule(posuvanie)

pyglet.app.run()