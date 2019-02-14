from furniture.animation import Animation
from drawBot import *

def draw(frame):
    fill(0)
    rect(*frame.page)
    
    y = pow(2 * frame.doneness - 1, 2)
    
    font("MotterPixturaVariable_v0001.ttf")
    fontVariations(wdth=(1-y)*1000, wght=500)
    fontSize(200)
    lineHeight(150)
    fill(y, 0, 1)
    text("Hello\nWorld", frame.page.offset(0, 50).center(), align="center")

animation = Animation(draw, length=60, fps=30, dimensions=(1000, 1000), burn=True)
animation.storyboard(frames=(0, 30, 59))