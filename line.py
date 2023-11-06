import cairo
def draw_new_polygon(ctx):
    ctx.move_to(50, 100)
    ctx.line_to(200,50)
    ctx.line_to(250,300)
    ctx.line_to(100,150)
    ctx.close_path()
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_new_line(ctx):
    ctx.move_to(0, 0)
    ctx.line_to(150, 100)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()

def  draw_open_polygon(ctx):
    ctx.move_to(50, 200)
    ctx.line_to(100,200)
    ctx.line_to(150,250)
    ctx.line_to(250,150)
    ctx.line_to(350,250)
    ctx.line_to(450,150)
    ctx.line_to(500,200)
    ctx.line_to(550,200)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_butt_cap(ctx):
    ctx.move_to(100, 80)
    ctx.line_to(500, 80)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(8)
    ctx.set_line_cap(cairo.LINE_CAP_BUTT)
    ctx.stroke()

def draw_square_cap(ctx):
    ctx.move_to(100, 200)
    ctx.line_to(500, 200)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_round_cap(ctx):
    ctx.move_to(100, 320)
    ctx.line_to(500, 320)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_width(10)
    ctx.stroke()

def draw_miter_join(ctx):
    ctx.move_to(50, 100)
    ctx.line_to(180, 300)
    ctx.line_to(50, 300)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.set_line_width(20)
    ctx.stroke()

def draw_round_join(ctx):
    ctx.move_to(240, 100)
    ctx.line_to(370, 300)
    ctx.line_to(240, 300)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.set_line_width(20)
    ctx.stroke()

def draw_bevel_join(ctx):
    ctx.move_to(430, 100)
    ctx.line_to(560, 300)
    ctx.line_to(430, 300)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
    ctx.set_line_width(20)
    ctx.stroke()    