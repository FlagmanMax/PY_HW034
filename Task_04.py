# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

import random
STR_SIZE = 20

def sort_(list_01):
    for i in range(STR_SIZE):
        for j in range(STR_SIZE-i-1):
            if list_01[j] > list_01[j+1]:
                (list_01[j], list_01[j+1]) = (list_01[j+1], list_01[j])


# list_01 = [random.randint(0, 100) for i in range(STR_SIZE)]
# print(list_01)
print(list_01 := [random.randint(0, 100) for i in range(STR_SIZE)])

sort_(list_01)
print(list_01)