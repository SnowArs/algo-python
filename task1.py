#Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#заданный случайными числами на промежутке [-100; 100). Выведите на экран
#исходный и отсортированный массивы. Сортировка должна быть реализована в виде
#функции. По возможности доработайте алгоритм (сделайте его умнее).

import random
import timeit
import cProfile

def sort():
    array = [random.randint(-100, 100) for i in range(50)]
    n = 1
    while n < len(array):
        for i in range(len(array)-n):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
        n += 1
    return array

def sort_python():
    array = [random.randint(-100, 100) for i in range(50)]
    return sorted(array)

#li = [random.randint(-100, 100) for i in range(50)]

##print('исходный массив: \n',li)
##print()
##print('отсортированный массив: \n', sort(li))
##print()
##print('отсортированный массив: \n', sort_python(li))

##print(timeit.timeit("sort()", setup="from __main__ import sort", number = 100000))
##print(timeit.timeit("sort_python()", setup="from __main__ import sort_python", number = 100000))

cProfile.run('sort()')
cProfile.run('sort_python()')

#результаты timeit.
## Видно, что пузырьковая сортировка на этих данных в 6 раз медленнее, чем стандартная функция сортировки массива в Python
##====== RESTART: C:\Users\membe\Desktop\geek\алгоритмы\lesson7\task1.py ======
##36.066013095
##6.8707697630000055
##====== RESTART: C:\Users\membe\Desktop\geek\алгоритмы\lesson7\task1.py ======
##35.066780067
##6.611583957999997

##cProfile, таких результатов не показывает, но видно, что при пузырьковой сортировке обращение к функции происходит гораздо чаще и ее работа занимает больше времени.
##====== RESTART: C:\Users\membe\Desktop\geek\алгоритмы\lesson7\task1.py ======
##         367 function calls in 0.002 seconds
##
##   Ordered by: standard name
##
##   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
##       50    0.000    0.000    0.000    0.000 random.py:174(randrange)
##       50    0.000    0.000    0.000    0.000 random.py:218(randint)
##       50    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
##        1    0.001    0.001    0.002    0.002 task1.py:10(sort)
##        1    0.000    0.000    0.000    0.000 task1.py:11(<listcomp>)
##        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
##       99    0.000    0.000    0.000    0.000 {built-in method builtins.len}
##       50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
##        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
##       63    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
##
##
##         266 function calls in 0.000 seconds
##
##   Ordered by: standard name
##
##   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
##       50    0.000    0.000    0.000    0.000 random.py:174(randrange)
##       50    0.000    0.000    0.000    0.000 random.py:218(randint)
##       50    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
##        1    0.000    0.000    0.000    0.000 task1.py:20(sort_python)
##        1    0.000    0.000    0.000    0.000 task1.py:21(<listcomp>)
##        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
##        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
##       50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
##        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
##       60    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
