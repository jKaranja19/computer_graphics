import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 700, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


def roundrect(ctx, x, y, width, height, r):
    ctx.arc(x+r, y+r,r, math.pi, 3*math.pi/2)
    ctx.arc(x+width-r,y+r,r,3*math.pi/2,0)
    ctx.arc(x+width-r,y+height-r,r, 0, math.pi/2)
    ctx.arc(x+r, y+height-r, r, math.pi/2,math.pi)
    ctx.close_path()


roundrect(ctx, 130, 90, 250, 450, 50)

def letter_A(ctx):
    ctx.move_to(165, 165)
    ctx.line_to(180, 100)
    ctx.line_to(195, 165)
    #ctx.new_sub_path()
    ctx.move_to(265, 205)
    ctx.line_to(180, 100)


letter_A(ctx)

ctx.set_line_width(1.17),
ctx.set_source_rgb(0, 0, 0.5)
ctx.stroke()


surface.write_to_png("roundrect.png")