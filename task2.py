import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0, 0, 0)
ctx.paint()

def draw_arc1(ctx):
    ctx.arc(400, 200,150, 0, math.pi)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(3.5)
    ctx.stroke()

def draw_arc2(ctx):
    ctx.arc(400, 500,150, math.pi, 0)
    ctx.set_source_rgb(0, 0, 1)
    ctx.set_line_width(3.5)
    ctx.stroke()

def draw_arc3(ctx):
    ctx.arc(550, 350,150, math.pi/2, 3*math.pi/2)
    ctx.set_source_rgb(0, 0, 1)
    ctx.set_line_width(3.5)
    ctx.stroke()

def draw_arc4(ctx):
    ctx.arc(250, 350,150, 3*math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(3.5)
    ctx.stroke()


draw_arc1(ctx)
draw_arc2(ctx)
draw_arc3(ctx)
draw_arc4(ctx)
surface.write_to_png("task2.png")