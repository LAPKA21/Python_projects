__author__ = 'Богушевич Д.А.'

VALUE_UP: float = 2.54 #Значение для перевода

def create_cm_to_inches_table(a: int) -> float:
    """Функция печати таблицы перевода см в дюймы,
     :param a: значение до которого выводится таблица
     """
    c:float = 0.0
    print("СМ   Дюймы")
    for i in range(a):
        c = c + VALUE_UP
        print(i + 1,"  ",round(c,2))

    return round(c,2)

#Проверка
assert create_cm_to_inches_table(10) == 25.4
assert create_cm_to_inches_table(5) == 12.7
assert create_cm_to_inches_table(1) == 2.54


