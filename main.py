from tkinter import *

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
check = Checkbutton(window, variable=state, text='Выбрать текстовый ввод', font=('Arial Bold', 12))
check.place(x=200, y=235)

# группа кнопок выбора определённых, заранее заданных цветов
lbl = Label(window, text='Или выбирете один из готовых:', font=('Arial', 14))
lbl.place(x=10, y=300)
btn_yellow = Button(window, text='Жёлтый', bg='yellow', bd=1,
                    height=3, width=10, font=('Arial Bold', 14),
                    activebackground='yellow', relief=RIDGE)
btn_yellow.place(x=10, y=350)
btn_pink = Button(window, text='Розовый', bg='#E6399B', bd=1,
                  height=3, width=10, font=('Arial Bold', 14),
                  activebackground='#E6399B', relief=RIDGE)
btn_pink.place(x=210, y=350)
btn_turquoise = Button(window, text='Бирюзовый', bg='#33CCCC', bd=1,
                       height=3, width=10, font=('Arial Bold', 14),
                       activebackground='#33CCCC', relief=RIDGE)
btn_turquoise.place(x=410, y=350)
btn_white = Button(window, text='Белый', bg='white', bd=1,
                   height=3, width=10, font=('Arial Bold', 14),
                   activebackground='white', relief=RIDGE)
btn_white.place(x=210, y=500)
btn_orange = Button(window, text='Оранжевый', bg='orange', bd=1,
                    height=3, width=10, font=('Arial Bold', 14),
                    activebackground='orange', relief=RIDGE)
btn_orange.place(x=10, y=500)
btn_black = Button(window, text='Чёрный', bg='black', bd=1,
                   height=3, width=10, font=('Arial Bold', 14),
                   activebackground='black', relief=RIDGE,
                   activeforeground='white', fg='white')
btn_black.place(x=410, y=500)

window.mainloop()
