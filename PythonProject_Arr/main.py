__author__ = 'Богушевич Д.А.'


from module_array import *
from file_module import *
import timeit


#Значения для интервала случайных чисел
A: int = 0 # Минимальное значение
B: int = 100000000 # Максимальное значение

N : int = 1000000 # Колличество элементов в массиве

NUMBER :int = 10
REPEAT: int = 1
#list_time = timeit.repeat(lambda: make_list_array(A,B,N), number=3, repeat=REPEAT)
set_time = timeit.repeat(lambda: make_set_array(A,B,N), number=NUMBER, repeat=REPEAT)
numpy_time = timeit.repeat(lambda: make_array_numpy(A,B,N), number=NUMBER, repeat=REPEAT)

#print(list_time)
print(set_time)
print(numpy_time)




