import cairo
import math
import rectangle
import line
import arc
import labwork
import curves
import sub_path
import arrow
import sec_seg


#setting up the interface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
context = cairo.Context(surface)
context.set_source_rgb(0.8, 0.8, 0.8)
context.paint()

#rectangle.draw_new_rectangle(ctx)
#line.draw_new_polygon(context)
#line.draw_new_line(context)
#line.draw_open_polygon(context)
#line.draw_butt_cap(context)
#line.draw_round_cap(context)
#line.draw_square_cap(context)

#To display the lines
#surface.write_to_png("lines.png")

#To display the arcs
#arc.draw_new_arc(context)
#arc.draw_small_circle(context)
#arc.draw_medium_circle(context)
#arc.draw_large_circle(context)

#curves.draw_bezier_curve(context)

#line.draw_round_join(context)
#line.draw_bevel_join(context)
#line.draw_miter_join(context)

#curves.draw_bezier_shape(context)

#labwork.draw_first_curve(context)

#sub_path.draw_sub_path_1(context)
#sub_path.draw_sub_path_2(context)
#sub_path.draw_sub_path_3(context)

#sec_seg.draw_arc(context)
#sec_seg.draw_sector(context)
#sec_seg.draw_segment(context)


surface.write_to_png("sec_seg.png")