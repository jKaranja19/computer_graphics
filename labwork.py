import cairo

def draw_first_curve(ctx):

    ctx.move_to(500, 150)
    ctx.curve_to(350, 400, 200, 200, 100, 300)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()