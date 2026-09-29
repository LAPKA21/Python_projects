__author__ = 'Богушевич Д.А.'

import random
from random import *
import numpy as np
import math as m
import timeit


def make_list_array(min:int, max:int, n:int) -> list :
    """
    Функция создания массива нечетных и не повторяющихся чисел с помощью list, модуля random, функции randint
    :param min: Минимальное значение диапозона случайных чисел
    :param max: Максимальное значение диапозона случайных чисел
    :param n: Количество элементов в массиве
    :return: Возвращает список заполненный случайными нечетными и не повторяющимися числами от min до max, количество элементов n
    """
    e: int = 0
    l: list = []
    while len(l) != n:
        e = randint(min, max)
        if e not in l and e % 2 != 0:
            l.append(e)
    return l

def make_set_array (min:int, max:int, n:int) -> set :
    """
    Функция создания массива нечетных и не повторяющихся чисел с помощью set, модуля random, функции randint
    :param min: Минимальное значение диапозона случайных чисел
    :param max: Максимальное значение диапозона случайных чисел
    :param n: Количество элементов в массиве
    :return: Возвращает множество заполненный случайными нечетными и не повторяющимися числами от min до max, количество элементов n
    """
    elem: int = 0
    a: set = set()
    while len(a) != n:
        elem = randint(min, max)
        a.add(elem)
    return a

def make_array_numpy (min:int, max:int, n:int) -> np.ndarray:
    """
    Функция создания массива нечетных и не повторяющихся чисел с помощью пакета numpy
    :param min: Минимальное значение диапозона
    :param max: Максимальное значение диапозона
    :param n: Количество элементов в массиве
    :return: Возвращает массив ndarray заполненный случайными нечетными и не повторяющимися числами от min до max, количество элементов n
    """
     # функция arrange в numpy создает одномерный массив с равномерно распределенными значениями в заданном диапазоне. Имеет следующие параметры:
     # arange([start, ]stop, [step, ]dtype=None) start (необязательно): начальное значение интервала (по умолчанию 0). stop: конечное значение интервала (в массив не включается).
     # step (необязательно): шаг изменения между соседними элементами (по умолчанию 1). dtype (необязательно): тип данных выходного массива. Если не указан, тип определяется автоматически.

    # функция choice используется для генерации случайной выборки из заданного одномерного массива или диапазона чисел. Имеет следующие параметры:
    # choice(a, size=None, replace=True, p=None) a (массив или целое число) — Источник для выборки, когда массив выбираем из его эдементов, когда число то диапозон от 0 до числа - 1
    # size (int или кортеж int, необязательный) — Форма выходного массива, Если None (по умолчанию), возвращается одно значение, если просто число то возращает вектор случайных чисел такой длины, можно использовать кортеж для матриц
    # replace (boolean, необязательный) — Флаг возвращения (повторения) элементов True - элементы повторяются, False - без повторов ВАЖНО --- в этом случае size не может превышать изначальную длинну элементов
    # p (массив, необязательный) — Вероятности, с которыми будет выбран каждый элемент.

    res = np.random.choice(np.arange(min if min % 2 != 0 else min + 1, max + 1, 2), n, replace=False)
    return res

def process_arr_pyt_sigmoind (l : list) -> float :
    """
    Функция обработки каждого элемента массива по формуле Сигмоиды и получения их суммы. Используются встроенные
    возможности питона и функции
    :param l: массив элементов
    :return: сумма обработанных элементов массива
    """
    s:float = 0.0
    for elem in l:
        s +=  1 / (1 + m.exp(-elem))
    return s


def process_arr_numpy_sigmoind (arr : np.ndarray) -> float :
    """
    Функция обработки каждого элемента массива по формуле Сигмоиды и получения их суммы. Используется функции из скаченной библиотека numpy
    :param arr: массив элементов
    :return: возвращает сумму обработанных элементов
    """
    return  np.sum(1 / (1 + np.exp (-np.array(arr))))

if __name__ == '__main__':


    a = make_list_array(0, 10, 5)
    assert len(a) == 5
    b = make_set_array(0, 10, 5)
    assert len(b) == 5
    c = make_array_numpy(0, 10, 5)
    assert len(c) == 5


    d: list = [1,2,3,4,5]
    assert round(process_arr_pyt_sigmoind(d), 2) == 4.54
    nump_arr: np.ndarray = np.arange(1,6)
    assert round(process_arr_numpy_sigmoind(nump_arr), 2) == 4.54
    arr_2:list = [-1,-2,-3,-4,-5]
    assert round(process_arr_pyt_sigmoind(arr_2), 2) == 0.46
    nump_arr_2: np.ndarray = np.arange(-5,0)
    assert round(process_arr_numpy_sigmoind(nump_arr_2), 2) == 0.46
    arr_3: list = [0,0,0,0,0]
    assert round(process_arr_pyt_sigmoind(arr_3), 2) == 2.5
    numpy_arr_zero: np.ndarray = np.zeros(5)
    assert round(process_arr_pyt_sigmoind(numpy_arr_zero), 2) == 2.5


