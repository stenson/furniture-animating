from furniture.animation import Animation
from drawBot import *

def draw(frame):
    fill(frame.doneness, 0, 0.5)
    rect(*frame.page)

animation = Animation(draw, length=60, fps=30, dimensions=(1000, 1000), fmt="pdf", burn=True)
animation.storyboard(frames=(0, 30, 59))