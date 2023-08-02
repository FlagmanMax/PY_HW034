# Hw_02
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
def dict_make(**kwargs):
    dict_01 = {}
    for key, value in kwargs.items():
        if not isinstance(value, int | bool | float | bool | tuple | frozenset):
            value_ = str(value)
        else:
            value_ = value
        dict_01[value_] = key
    return dict_01

a = 123
b = 'Hello'
c = True
d = [1, 2, 3]

print(dict_make(a=123, b='Hello', c=True, d=[1, 2, 3]))
