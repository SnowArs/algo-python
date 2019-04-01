##Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
##Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Задача 7 из урока 2

import timeit
import cProfile

def without_recur(n):
        sum2 = 0
        i = 1

        while i <= n:
                sum2 += i
                i += 1
        return sum2

	
def recur(n):
        sum1 = 0
        if n > 2:
                sum1 = recur(n-1) + n
        return sum1 


print(timeit.timeit("without_recur(100)", setup="from __main__ import without_recur", number = 100000))
print(timeit.timeit("recur(100)", setup="from __main__ import recur", number = 100000))

##cProfile.run('without_recur(100)')
##cProfile.run('recur(100)')

#timeit показывает более или менее похожие числа при вычислении 10 значений, но при увеличении чисел на порядок время вычесления рекурсии увеличивается в 2 раза -> из за сложности рекурсии
##====== RESTART: C:/Users/membe/Desktop/geek/алгоритмы/lesson4/task01.py ======
##0.10659461699999995
##0.170523627
##>>> 
##====== RESTART: C:/Users/membe/Desktop/geek/алгоритмы/lesson4/task01.py ======
##0.12528671399999997
##0.1526571029999999
##>>> 
##====== RESTART: C:/Users/membe/Desktop/geek/алгоритмы/lesson4/task01.py ======
##0.131321731
##0.14998966700000005


##cProfile особых задержек между алгоритмами не показывает, скорее всего из за простоты кода) хотя видно что при рекурсии количество обращении к функции гораздо больше.
##====== RESTART: C:/Users/membe/Desktop/geek/алгоритмы/lesson4/task01.py ======
##         4 function calls in 0.000 seconds
##
##   Ordered by: standard name
##
##   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
##        1    0.000    0.000    0.000    0.000 task01.py:4(without_recur)
##        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
##        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
##
##
##         102 function calls (4 primitive calls) in 0.000 seconds
##
##   Ordered by: standard name
##
##   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
##     99/1    0.000    0.000    0.000    0.000 task01.py:14(recur)
##        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
##        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
