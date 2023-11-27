from tkinter import *

from tkinter import ttk
root = Tk()
canvas = Canvas(root)
# canvas.pack()

color_primary_100="#00BFA5"
color_primary_200="#00a189"
color_primary_300="#005f4b"
color_accent_100="#FF4081"
color_accent_200="#ffe4ff"
color_text_100="#FFFFFF"
color_text_200="#e0e0e0"
color_bg_100="#1A1A1A"
color_bg_200="#292929"
color_bg_300="#404040"


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


x1 = 50
y1 = 100
width = 100
height = 50
frame = Frame(root)
frame.grid(row=0, column=0)

canvas = Canvas(frame, width=300, height=200)
canvas.grid(row=0, column=0)

my_rectangle = round_rectangle(x1, y1, x1+width, y1+height,  radius=20, fill='',outline='black', width=2)

entry = Entry(root)
entry.place(x=x1+10, y=y1+10, width=width-20, height=height-20)

root.configure(bg=color_bg_300)
root.mainloop()