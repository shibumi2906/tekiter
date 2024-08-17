#Напишите программу на Python с использованием модуля tkinter,
# которая позволяет пользователю ввести свое имя в окно ввода,
# а затем выводит на экран сообщение "Привет, [имя]!".

import tkinter as tk

def greet():
    name = entry.get()
    greeting_label.config(text=f"Привет, {name}!")

root = tk.Tk()
root.title("Приветствие")

label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Поприветствовать", command=greet)
button.pack(pady=10)

greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

root.mainloop()


