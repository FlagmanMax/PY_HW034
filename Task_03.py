# Task_03
#  Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def dict_create(string_input: str):

    beg, end = sorted(string_input.split())

    # dict_01 = {ord(x):x for x in range(int(beg), int(end)+1)}

    return dict({ord(str(x)): x for x in range(int(beg), int(end)+1)})

print(dict_create('7 3'))