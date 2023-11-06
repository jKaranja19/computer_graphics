#This is for sector and segment :)

import cairo
import math

#def draw_arc(ctx):
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 0.8, 0.8)
ctx.paint()
ctx.set_line_width(10),
ctx.set_source_rgb(0, 0, 0.5)
 
ctx.arc(200, 200, 150, 3*math.pi/4, 5*math.pi/4)


ctx.new_sub_path()
ctx.arc(350, 200, 150, 3*math.pi/4, 5*math.pi/4)
ctx.close_path()


ctx.move_to(500, 200)
ctx.arc(500, 200, 150, 3*math.pi/4, 5*math.pi/4)
ctx.close_path()

ctx.stroke()

surface.write_to_png("sec_seg.png")
