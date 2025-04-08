
# 🧠 WortChecker — тренажёр немецких слов

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![customtkinter](https://img.shields.io/badge/GUI-customtkinter-blueviolet)
![Status](https://img.shields.io/badge/status-active-brightgreen)

## 📚 Описание

**WortChecker** — это графическое приложение на Python для тренировки перевода немецких слов на русском языке.  
Программа показывает слово по-русски, а пользователь должен ввести правильный перевод на немецком. После нажатия на кнопку «Проверить» приложение сообщает, правильно ли дан ответ.

---

## 🚀 Возможности
- Перевод слов с помощью **DeepL API**
- Проверка правильности ввода
- Подсказка по нажатию на «Ключ к решению»
- Красивый интерфейс на `customtkinter`
- Отображение позитивных и негативных сообщений

---

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ТВОЙ_НИК/WortChecker.git
cd WortChecker
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте `.env` файл и добавьте туда ваш ключ DeepL API:

```
API_KEY=ваш_ключ_deepl
```

4. Запустите программу:
```bash
python main.py
```

---

## 🧩 Зависимости

- `customtkinter`
- `tkinter`
- `Pillow`
- `python-dotenv`
- `requests`

> Установите всё сразу:
```bash
pip install customtkinter pillow python-dotenv requests
```

---

## 📂 Структура проекта

```
WortChecker/
├── allworts.txt
├── main.py
├── .env
├── .gitignore
├── fon.jpg
├── info.png
└── README.md
```

---

## 👨‍💻 Об авторе

**Андрей**  
Я не профессиональный разработчик, а просто человек, которому интересна разработка и изучение новых технологий.  
Этот проект — часть моего пути в изучении Python и создания графических интерфейсов.

📬 andreirtt9@gmail.com  
📨 Telegram: [@kypich](https://t.me/kypich)

---

## 🔗 Лицензия

MIT License. Используйте свободно, но не забывайте о ссылке на автора 😉
