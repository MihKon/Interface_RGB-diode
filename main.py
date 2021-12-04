from tkinter import *

window = Tk()
window.title('Изменение цвета RGB-светодиода')
window.geometry('600x400')
window.resizable(width=False, height=False)

lbl_red = Label(window, text='RED:', font=('Arial Bold', 20), foreground='red')
lbl_red.place(x=10, y=9)
lbl_blue = Label(window, text='BLUE:', font=('Arial Bold', 20), foreground='blue')
lbl_blue.place(x=10, y=89)
lbl_green = Label(window, text='GREEN:', font=('Arial Bold', 20), foreground='green')
lbl_green.place(x=10, y=169)

red_scale = Scale(window, from_=0, to=200, resolution=1,
                  orient=HORIZONTAL, troughcolor='red', length=200)
red_scale.place(x=200)
blue_scale = Scale(window, from_=0, to=200, resolution=1,
                   orient=HORIZONTAL, troughcolor='blue', length=200)
blue_scale.place(x=200, y=80)
green_scale = Scale(window, from_=0, to=200, resolution=1,
                    orient=HORIZONTAL, troughcolor='green', length=200)
green_scale.place(x=200, y=160)

window.mainloop()
