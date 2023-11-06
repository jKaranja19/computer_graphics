#Drawing the image inside the previously created rectangle
def draw_rectangle(context):
    context.rectangle(150, 100, 100, 240)
    context.set_source_rgb(1, 0, 0)
    context.fill()


def draw_new_rectangle(ctx):
    ctx.rectangle(300, 200, 200, 340)
    ctx.set_source_rgb(0, 1, 0)
    ctx.fill()


