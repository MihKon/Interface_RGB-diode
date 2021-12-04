from tkinter import *
from functools import partial
from gpiozero import PWMLED


# функции реагирования
def check_clicked():
    if state.get():
        txt_red.config(state='normal')
        txt_blue.config(state='normal')
        txt_green.config(state='normal')
        red_scale.config(state='disabled')
        blue_scale.config(state='disabled')
        green_scale.config(state='disabled')
    else:
        txt_red.config(state='disabled')
        txt_blue.config(state='disabled')
        txt_green.config(state='disabled')
        red_scale.config(state='normal')
        blue_scale.config(state='normal')
        green_scale.config(state='normal')


def set_color(value, color):
    if color == 'red':
        red.value = float(value) / 255
        txt_red.config(state='normal')
        txt_red.delete(0, END)
        txt_red.insert(0, value)
        txt_red.config(state='disabled')
    elif color == 'green':
        green.value = float(value) / 255
        txt_green.config(state='normal')
        txt_green.delete(0, END)
        txt_green.insert(0, value)
        txt_green.config(state='disabled')
    elif color == 'blue':
        blue.value = float(value) / 255
        txt_blue.config(state='normal')
        txt_blue.delete(0, END)
        txt_blue.insert(0, value)
        txt_blue.config(state='disabled')


def change_button_color(color):
    if color == 'yellow':
        red.value = 1
        green.value = 1
        blue.value = 0
    elif color == 'pink':
        red.value = 1
        green.value = 0
        blue.value = 1
    elif color == 'turquoise':
        red.value = 0
        green.value = 1
        blue.value = 1
    elif color == 'white':
        red.value = 1
        green.value = 1
        blue.value = 1
    elif color == 'orange':
        red.value = 1
        green.value = 0.5
        blue.value = 0
    elif color == 'black':
        red.value = 0
        green.value = 0
        blue.value = 0


red = PWMLED(23)
green = PWMLED(24)
blue = PWMLED(25)

# окно приложения
window = Tk()
window.title('Изменение цвета RGB-светодиода')
window.geometry('540x600')
window.resizable(width=False, height=False)

# подписи к скроллбарам и текстовым полям
lbl_red = Label(window, text='RED:', font=('Arial Bold', 20), foreground='red')
lbl_red.place(x=10, y=9)
lbl_green = Label(window, text='GREEN:', font=('Arial Bold', 20), foreground='green')
lbl_green.place(x=10, y=89)
lbl_blue = Label(window, text='BLUE:', font=('Arial Bold', 20), foreground='blue')
lbl_blue.place(x=10, y=169)

# скроллбары изменения цвета
red_scale = Scale(window, from_=0, to=255, resolution=1,
                  orient=HORIZONTAL, troughcolor='red', length=200, command=partial(set_color, color='red'))
red_scale.place(x=200)
green_scale = Scale(window, from_=0, to=255, resolution=1,
                    orient=HORIZONTAL, troughcolor='green', length=200, command=partial(set_color, color='green'))
green_scale.place(x=200, y=80)
blue_scale = Scale(window, from_=0, to=255, resolution=1,
                   orient=HORIZONTAL, troughcolor='blue', length=200, command=partial(set_color, color='blue'))
blue_scale.place(x=200, y=160)

# текстовые поля ввода яркости цвета
txt_red = Entry(window, width=10, state='disabled')
txt_red.place(x=460, y=20)
txt_green = Entry(window, width=10, state='disabled')
txt_green.place(x=460, y=100)
txt_blue = Entry(window, width=10, state='disabled')
txt_blue.place(x=460, y=180)

# кнопка активации текстового ввода
state = BooleanVar()
check = Checkbutton(window, variable=state, text='Выбрать текстовый ввод',
                    font=('Arial Bold', 12), command=check_clicked)
check.place(x=200, y=235)

# группа кнопок выбора определённых, заранее заданных цветов
lbl = Label(window, text='Или выбирете один из готовых:', font=('Arial', 14))
lbl.place(x=10, y=300)
btn_yellow = Button(window, text='Жёлтый', bg='yellow', bd=1,
                    height=3, width=10, font=('Arial Bold', 14),
                    activebackground='yellow', relief=RIDGE, command=partial(change_button_color, 'yellow'))
btn_yellow.place(x=10, y=350)
btn_pink = Button(window, text='Розовый', bg='#E6399B', bd=1,
                  height=3, width=10, font=('Arial Bold', 14),
                  activebackground='#E6399B', relief=RIDGE, command=partial(change_button_color, 'pink'))
btn_pink.place(x=210, y=350)
btn_turquoise = Button(window, text='Бирюзовый', bg='#33CCCC', bd=1,
                       height=3, width=10, font=('Arial Bold', 14),
                       activebackground='#33CCCC', relief=RIDGE, command=partial(change_button_color, 'turquoise'))
btn_turquoise.place(x=410, y=350)
btn_white = Button(window, text='Белый', bg='white', bd=1,
                   height=3, width=10, font=('Arial Bold', 14),
                   activebackground='white', relief=RIDGE, command=partial(change_button_color, 'white'))
btn_white.place(x=210, y=500)
btn_orange = Button(window, text='Оранжевый', bg='orange', bd=1,
                    height=3, width=10, font=('Arial Bold', 14),
                    activebackground='orange', relief=RIDGE, command=partial(change_button_color, 'orange'))
btn_orange.place(x=10, y=500)
btn_black = Button(window, text='Чёрный', bg='black', bd=1,
                   height=3, width=10, font=('Arial Bold', 14),
                   activebackground='black', relief=RIDGE,
                   activeforeground='white', fg='white', command=partial(change_button_color, 'black'))
btn_black.place(x=410, y=500)

window.mainloop()
