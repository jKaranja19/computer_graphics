import cairo

def draw_sub_path_1(ctx):
    ctx.set_source_rgb(1, 0, 1)
    ctx.set_line_width(10)
    ctx.move_to(50, 50),
    ctx.line_to(400, 200),
    ctx.line_to(50, 350),
    ctx.close_path()
    ctx.stroke()    

def draw_sub_path_2(ctx):
    ctx.set_source_rgb(1, 0, 1)
    ctx.set_line_width(10)
    ctx.move_to(450, 100),
    ctx.line_to(550, 100),
    ctx.line_to(450, 300),
    ctx.close_path()
    ctx.stroke()


def draw_sub_path_3(ctx):
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.move_to(100, 100),
    ctx.line_to(200, 200),
    ctx.line_to(100, 300),
    ctx.close_path()
    ctx.stroke()