# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

from pprint import pprint

def dict_01(names, pays, percents):
    percents = list(map(lambda x: float(x[:-1])/100, percents))
    return {name: pay*percent for name, pay, percent in zip(names, pays, percents)}

names = ["Иван", "Петр", "Михаил"]
pays = [10000, 15000, 20000]
percents = ["50.01%", "20.15%", "30"]

dict_02 = dict_01(names, pays, percents)
pprint(dict_02)
