from furniture.animation import Animation
from drawBot import *

def draw(frame):
    fill(frame.doneness, 0, 0.5)
    # frame.doneness is a 0-1 value that we pass directly
    # to the "red" channel of this rgb function, so the
    # color will move from having no red to having full red
    rect(*frame.page)

animation = Animation(draw, length=60, fps=30, dimensions=(1000, 1000), burn=True)
animation.storyboard(frames=(0, 30, 59))