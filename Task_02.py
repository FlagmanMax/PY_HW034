# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def str_control(string_input):
    return sorted(set(map(ord, list(string_input))), reverse=True)

print(str_control(input("Введите строку:")))