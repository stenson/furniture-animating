# RUN: python -c 'import bonus; bonus.animation.render()'
from furniture.animation import Animation
from furniture.vfont import scale_to_axis
from drawBot import *

def draw(frame, zoom=False):
    def draw_text(t1, t2):
        font("MotterPixturaVariable_v0001.ttf")
        axes = listFontVariations()
        wdth = axes.get("wdth")
        wght = axes.get("wght")
    
        fontSize(200)
        lineHeight(200)
        y = pow(2 * frame.doneness - 1, 2)
    
        fea = dict()
        if frame.i > 15:
            fea["ss03"] = True
        if frame.i > 30:
            fea["dlig"] = True
            fea["ss02"] = True
        if frame.i > 41:
            fea["ss01"] = True
        openTypeFeatures(**fea)
    
        fontVariations(
            wght=scale_to_axis(wght, 1-y),
            wdth=scale_to_axis(wdth, y))
        fill(y, 0.3, 0.7, 1)
        text(t1, (500, 550), align="center")
    
        fontVariations(
            wght=scale_to_axis(wght, y),
            wdth=scale_to_axis(wdth, 1-y))
        fill(0, 0.5+y/2, 0.5-y, 1)
        text(t2, (500, 550), align="center")
    
    fill(0)
    rect(*frame.page)
    with savedState():
        translate(0, 0)
        scale(6, center=frame.page.center())
        draw_text(
            "FURNITURE.\nANIMATION",
            "PYTHON\nCODE")
    draw_text(
        "HELLO\n{:02d} FRAMES".format(frame.i),
        "animating\nwith drawbot")

animation = Animation(draw, 60, 30, (1000, 1000))
animation.storyboard(frames=(0, 30, 59))