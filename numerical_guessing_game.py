import random
from tkinter import *

root = Tk()

win_num = random.randint(1, 100)

def is_valid(n):
    try:
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    except ValueError:
        return False

def gues_num():
    inp_num = cityField.get()
    if is_valid(inp_num):
        inp_num = int(inp_num)
        if inp_num == win_num:
            info['text'] = f'Поздравляю, вы успешно угадали число: {win_num}'
            root.after(5000, root.destroy)
        elif inp_num < win_num:
            info['text'] = 'Ваше число меньше загаданного, попробуйте ещё раз'
        else:
            info['text'] = 'Ваше число больше загаданного, попробуйте еще разок'
    else:
        info['text'] = 'А может быть все-таки введем целое число от 1 до 100?'

root['bg'] = '#34CFBE'
root.title('Числовая угадайка')
root.geometry('500x300')

frame_top = Frame(root, bg='#1E776D', bd=10, relief='sunken')
frame_top.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.3)

frame_bottom = Frame(root, bg='#009E8E', bd=10, relief='sunken')
frame_bottom.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.3)

cityField = Entry(frame_top, bg='#00675C', font=('Arial', 14))
cityField.pack()

btn = Button(frame_top, text='Введите число', command=gues_num)
btn.pack()

info = Label(frame_bottom, text='Число загадано!', bg='white', font=('Arial', 14), fg='green')
info.pack()

root.mainloop()  # Запускаем постоянный цикл, чтобы программа работала