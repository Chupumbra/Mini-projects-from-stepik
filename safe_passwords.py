import random
from tkinter import *

root = Tk()


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

quan = int(input('Введите количество паролей для генерации: '))
lenght = int(input('Введите длину паролей: '))

di = input('Пароль должен включать цифры? (да/нет): ')
ll = input('Пароль должен включать прописные буквы? (да/нет): ')
ul = input('Пароль должен включать строчные буквы? (да/нет): ')
p = input('Пароль должен включать символы: "!#$%&*+-=?@^_"? (да/нет): ')
neod = input('Пароль должен исключать неоднозначные символы: "il1Lo0O"? (да/нет): ')

if di == 'да':
    chars += random.choice(digits)
if ll == 'да':
    chars += random.choice(lowercase_letters)
if ul == 'да':
    chars += random.choice(uppercase_letters)
if p == 'да':
    chars += random.choice('il1Lo0O')

def generate_pas(lenght, chars):
    pas = ''
    for i in range(lenght):
        pas += random.choice(chars)
    return pas

for j in range(quan):
    pas = generate_pas(lenght, chars)
    print(pas)