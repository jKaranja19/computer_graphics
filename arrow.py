import cairo
import math

def arrow(ctx, x, y, width, height, a, b):
    ctx.move_to(x, y+b)
    ctx.line_to(x, y+height-b)
    ctx.line_to(x+a,y+height-b)
    ctx.line_to(x+a, y+height)
    ctx.line_to(x+width, y+height/2)
    ctx.line_to(x+a, y)
    ctx.line_to(x+a, y+b)
    ctx.fill()