from customtkinter import*
from tkinter import messagebox
import tkinter as tk
from PIL import Image
import requests
from dotenv import load_dotenv
import random
import os
import sys

load_dotenv()

def center_window(window, width, height):
    # Получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Вычисляем координаты для центрирования окна
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Устанавливаем геометрию окна
    window.geometry(f'{width}x{height}+{x}+{y}')

window_width = 950
window_height = 600

app = CTk()
app.geometry('950x600')
app.title('Check your skills')
app.resizable(width=False, height=False)
app.configure(fg_color='#301867')
set_appearance_mode('#030030')
center_window(app, window_width, window_height)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def choice_word():
    # with open('allworts.txt', 'r', encoding='utf-8') as file:
    #     words = [line.strip() for line in file if line.strip()]
    file_path = resource_path('allworts.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
            
    word = random.choice(words)
    print(word)
    return word

def translate(text):
    api_key = os.getenv("API_KEY")
    url = 'https://api-free.deepl.com/v2/translate'
    params = {'auth_key': api_key, 'text': text, 'source_lang': 'De', 'target_lang': 'Ru'}
    
    response = requests.post(url, data=params)
    result = response.json() # {'translations': [{'detected_source_language': 'NB', 'text': 'Здравствуйте'}]}
    
    res = result['translations'][0]['text']
    return res

def check_word(key_word, answer):
    return key_word == answer
    
key_word = choice_word()   # тут лежит слово на немецком

def button_check():
    global key_word
    user_input = entry.get().strip().lower()
    tempkey = key_word.lower()
    
    if not check_word(tempkey, user_input):
        negativ_messages = ["Попробуй еще раз!", "Не совсем так, попробуй снова.", "Неправильно, попробуй еще раз.", "Ответ неверный, попробуй снова!", "Не совсем верно, попробуй еще раз.", "Упс, не то! Давай попробуем снова.", "Не сдавайся, попробуй еще раз!", "Это не тот ответ. Попробуй снова!", "Ошибочка, попробуй еще раз.", "Неправильно, но у тебя всё получится! Еще раз?"]
        textfail = random.choice(negativ_messages)
        title.configure(text=textfail)
    if check_word(tempkey, user_input):
        positive_messages = ["Поздравляем!", "Отлично!", "Правильно!", "Замечательно!", "Вы справились!", "Превосходно!", "Молодец!", "Верно!"]
        textfail = random.choice(positive_messages)
        title.configure(text=textfail)

        entry.delete(0, END)  # <<< Очищает поле ввода

        key_word = choice_word()
        label_word.configure(text=translate(key_word))
        title_hint.configure(text='')
    
def button_answer():
    global key_word
    
    title_hint.configure(text=key_word)
    
def show_info():
    # Создание нового окна (диалогового окна)
    info_window = CTkToplevel()
    info_window.geometry("400x300")
    info_window.title("Информация обо мне")
    
    # Добавление текста в новое окно
    info_label = CTkLabel(info_window, text="Ваше Имя\nДолжность или занятие\nЛюбая другая информация", 
                          font=('Franklin Gothic Medium', 18), text_color='black')
    info_label.pack(pady=20)  # Добавляем отступы
    
    # Добавление кнопки для закрытия окна
    close_button = CTkButton(info_window, text="Закрыть", command=info_window.destroy)
    close_button.pack(pady=10)

def show_about():
    about_message = (
        "Обо мне:\n"
        "Имя: Aндрей\n"
        "Род деятельности: Разработчик ПО\n\n"
        "Контакты:\n"
        "Email: andreirtt9@gmail.com\n"
        "Telegram: @kypich\n\n"
        "Описание:\n"
        "Я увлекаюсь разработкой программного обеспечения и работаю над различными проектами, связанными с обучением и автоматизацией.\n\n"
        "По вопросам программы, обнаруженным ошибкам, багам или предложениям по улучшению пишите на почту или в Telegram."
    )
    messagebox.showinfo("Обо мне", about_message)
    
    
image_path = resource_path('fon.jpg')
pil_image = Image.open(image_path)

icon_path = resource_path('info.png')
img_icon = Image.open(icon_path)
    
ctk_image = CTkImage(light_image=pil_image, size=(448, 888))

label_image = CTkLabel(app, text="", image=ctk_image)
label_image.place(relx=0.23, rely=0.26, anchor='center')

frame = CTkFrame(master=app, width=450, height=600, fg_color='#030030')
frame.place(relx=0.5, rely=0.5, anchor='center')

# невидимый задний фон под фразами messages (негатив позитив)
title = CTkLabel(master=app, text="", width=300, height=50, font=('Franklin Gothic Medium', 18), bg_color='#030030', text_color='white')
title.place(relx=0.5, rely=0.6, anchor='center')

# невидимый задний фон под ответом (hint)
title_hint = CTkLabel(master=app, text="", width=300, height=50, font=('Franklin Gothic Medium', 18), bg_color='#030030', text_color='#7649e7')
title_hint.place(relx=0.5, rely=0.69, anchor='center') 

# сделать все подобным батону (но подвинуть нужно еще)
button = CTkButton(master=app, text="Проверить", width=200, height=50, font=('Franklin Gothic Medium', 18), hover_color='#ac36e3', fg_color='#9e78ed', command=button_check)
button.place(relx=0.5, rely=0.8, anchor='center') 

button_hint = CTkButton(master=app, text="Ключ к решению", width=450, height=40, font=('Franklin Gothic Medium', 18), hover_color='#ac36e3', fg_color='#9e78ed', command=button_answer)
button_hint.place(relx=0.5, rely=0.97, anchor='center')   

# задний фон на фрейме
framefront = CTkFrame(master=app, width=300, height=200, fg_color='#301867', border_color='#7649e7', border_width=2)
framefront.place(relx=0.5, rely=0.35, anchor='center')

# Создание поля для ввода (аналог Entry в tkinter)  # почти реди
entry = CTkEntry(master=app, placeholder_text="Введите текст здесь", width=225, height=50, font=('Franklin Gothic Medium', 20), fg_color='#9e78ed', text_color='white', placeholder_text_color='white', border_color='#7649e7')
entry.place(relx=0.5, rely=0.45, anchor='center')

# еще не реди
label_word = CTkLabel(master=app, text=f"{translate(key_word)}", width=20, height=20, font=('Franklin Gothic Medium', 25), fg_color='#301867', wraplength=290)
label_word.place(relx=0.5, rely=0.25, anchor='center')

# еще не реди (почти)   
label_text = CTkLabel(master=app, text='Введите правильный перевод: ', width=270, height=50, font=('Franklin Gothic Medium', 27), fg_color='#030030', text_color='#9e78ed')
label_text.place(relx=0.5, rely=0.1, anchor='center')


instructions = """
Как использовать:


Показ слова: В центре отображается слово на русском.

Ввод перевода: Введите немецкий перевод слова в текстовое поле.

Проверка: Нажмите "Проверить" для проверки перевода.

Результат: Программа сообщит, правильный ли ваш ответ.


Примечание: Для корректной работы программы необходимо стабильное интернет-соединение.
"""
label_instructions = CTkLabel(master=app, text=instructions, font=('Franklin Gothic Medium', 17), fg_color='#301867', text_color='white', wraplength=240, justify=LEFT)
label_instructions.place(relx=0.87, rely=0.5, anchor='center')

info_button = CTkButton(app, text="INFO", width=50, height=20, font=('Franklin Gothic Medium', 18), hover_color='#ac36e3', fg_color='#030030', image=CTkImage(dark_image=img_icon, light_image=img_icon), command=show_about)
info_button.place(relx=0.87, rely=0.96, anchor='center')

entry.bind('<Return>', lambda event: button_check())

app.mainloop()
