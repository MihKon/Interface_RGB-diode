from tkinter import *
from tkinter.ttk import Radiobutton

window = Tk()
window.title('Изменение цвета RGB-светодиода')
window.geometry('600x400')
window.resizable(width=False, height=False)

# подписи к скроллбарам и текстовым полям
lbl_red = Label(window, text='RED:', font=('Arial Bold', 20), foreground='red')
lbl_red.place(x=10, y=9)
lbl_green = Label(window, text='GREEN:', font=('Arial Bold', 20), foreground='green')
lbl_green.place(x=10, y=89)
lbl_blue = Label(window, text='BLUE:', font=('Arial Bold', 20), foreground='blue')
lbl_blue.place(x=10, y=169)

# скроллбары изменения цвета
red_scale = Scale(window, from_=0, to=200, resolution=1,
                  orient=HORIZONTAL, troughcolor='red', length=200)
red_scale.place(x=200)
green_scale = Scale(window, from_=0, to=200, resolution=1,
                    orient=HORIZONTAL, troughcolor='green', length=200)
green_scale.place(x=200, y=80)
blue_scale = Scale(window, from_=0, to=200, resolution=1,
                   orient=HORIZONTAL, troughcolor='blue', length=200)
blue_scale.place(x=200, y=160)

# текстовые поля ввода яркости цвета
txt_red = Entry(window, width=10)
txt_red.place(x=460, y=20)
txt_blue = Entry(window, width=10)
txt_blue.place(x=460, y=100)
txt_green = Entry(window, width=10)
txt_green.place(x=460, y=180)

# кнопка активации текстового ввода
state = BooleanVar()
check = Checkbutton(window, variable=state, text='Выбрать текстовый ввод', font=('Arial Bold', 14))
check.place(x=10, y=240)

window.mainloop()
