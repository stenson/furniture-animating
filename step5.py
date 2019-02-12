from furniture.animation import Animation
from furniture.vfont import scale_to_axis
from drawBot import *

def draw(frame):
    fill(0)
    rect(*frame.page)
    
    font("Obviously Variable")
    t1 = "HALLO\nWERELD"
    t2 = "kumusta\nmundo!"
    axes = listFontVariations()
    wdth = axes.get("wdth")
    wght = axes.get("wght")
    
    fontSize(200)
    lineHeight(200)
    y = pow(2 * frame.doneness - 1, 2)
    
    translate(0, -50*y)
    with savedState():
        translate(0, 110*(y))
        fontVariations(
            wght=scale_to_axis(wght, 1-y),
            wdth=scale_to_axis(wdth, 1-y))
        fill(y, 0.3, 0.7, 1)
        text(t1, (500, 550), align="center")
    
    fontVariations(
        wght=scale_to_axis(wght, y),
        wdth=scale_to_axis(wdth, 1-y))
    fill(1)
    text(t2, (500, 550), align="center")

animation = Animation(draw, 60, 30, (1000, 1000), fmt="pdf")
animation.storyboard(frames=(0, 30, 59))