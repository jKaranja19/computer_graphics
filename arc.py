import cairo
import math

def draw_new_arc(ctx):
    ctx.arc(300, 200,150, 0, math.pi/2)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_small_circle(ctx):
    ctx.arc(300, 200,50, 0, 2*math.pi)
    ctx.set_source_rgb(1, 0, 1)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_medium_circle(ctx):
    ctx.arc(300, 200, 150, 0, 2*math.pi)
    ctx.set_source_rgb(1, 0, 1)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_large_circle(ctx):
    ctx.arc(300, 200, 300, 0, 2*math.pi)
    ctx.set_source_rgb(1, 0, 1)
    ctx.set_line_width(10)
    ctx.stroke()