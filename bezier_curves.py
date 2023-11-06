import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ax=150
ay=150

bx=50
by=50

cx=205
cy=90

dx=255
dy=150

ctx.move_to(ax, ay)
ctx.curve_to(bx, by, cx, cy, dx, dy)
ctx.set_line_width(4.87),
ctx.set_source_rgb(1, 0, 0)
ctx.stroke()


surface.write_to_png("bezier_curve.png")