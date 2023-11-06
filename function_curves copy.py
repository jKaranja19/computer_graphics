import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

x=0 
points = []
while x < 5:
    y=math.sin(10 * x)*math.exp(-x/2)
    points.append((x*100+50, y*100+200))
    x+=0.01

ctx.move_to(*points[0])
for p in points[1:]:
    ctx.line_to(*p)
ctx.set_line_width(2.87),
ctx.set_source_rgb(0, 0, 0.5)
ctx.stroke()


surface.write_to_png("function_curves.png")