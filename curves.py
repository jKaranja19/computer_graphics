import cairo

def draw_bezier_curve(ctx):
    #ctx.move_to(100, 100)
    #ctx.curve_to(200, 100, 100, 100, 50, 150)
    ctx.move_to(500, 300)
    ctx.curve_to(350, 400, 200, 200, 100, 300)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_bezier_shape(ctx):
    ctx.move_to(100, 100)
    ctx.curve_to(200, 0, 400, 200, 500, 100)
    ctx.line_to(500, 300)
    ctx.curve_to(400, 400, 200, 200, 100, 300)
    ctx.close_path()
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.set_dash([40, 10])
    ctx.stroke()