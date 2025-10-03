import random
from tkinter import *

root = Tk() #создание окна приложения

answer = ['Бесспорно', "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
          "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "знаки говорят - да", "Да",
          "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя подсказать", "Сконцентрируйся и спроси опять",
          "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]


def get_answer():
    question = cityField.get()
    if question.lower() == 'стоп':
        info['text'] = 'Возвращайся если возникнут вопросы!'
        root.after(2000, root.destroy) #закрыть окно через 2 сек
    else:
        random_answer = random.choice(answer)
        info['text'] = f'Ответ на ваш вопрос: {random_answer}'

root['bg'] = '#CB60D3'
root.title('Магический шар')
root.geometry('400x300')
#root.resizable(width=False, height=False) - пользователю нельзя будет изменять размер окна

frame_top = Frame(root, bg='#8942D6', bd=8)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#8942D6', bd=8)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='#9D69D6', font=('Arial', 14))
cityField.pack()

btn = Button(frame_top, text='Задать вопрос', command=get_answer)
btn.pack()

info = Label(frame_bottom, text='Ответ на ваш вопрос', bg='#8942D6', font=('Arial', 14))
info.pack()

root.mainloop() # Запускаем постоянный цикл, чтобы программа работала
