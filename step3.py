from furniture.animation import Animation
from drawBot import *

def draw(frame):
    fill(0)
    rect(*frame.page)
    
    y = pow(2 * frame.doneness - 1, 2)
    
    font("Obviously Variable")
    fontSize(200)
    lineHeight(200)
    fill(y, 0, 0.5)
    text("Hello", frame.page.offset(0, -300*(1-y)-40).center(), align="center")

animation = Animation(draw, length=60, fps=30, dimensions=(1000, 1000), burn=True)
animation.storyboard(frames=(0, 30, 59))