#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.


"""похитил алгоритм в сети, метод слияния мы вроде как не проходили на уроке!!!"""

import random

@profile 
def merge(left, right):

    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst
@profile  
def mergesort(lst):
    

    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst
@profile 
def sort_python(lst):
    return sorted(lst)

##li = [random.uniform(0, 50) for i in range(20)]
##
##print('исходный массив: \n',li)
##print()
##print('отсортированный массив: \n', mergesort(li))


if __name__ == '__main__':
    lst = [random.uniform(0, 50) for i in range(20)]
    mergesort(lst)
    sort_python(lst)
    
## Если я правильно разобрался, то получается, что "метод слияния" использует две
## функции занимая в два раза больше памяти, чем стандартная функция Python, хотя не уверен до конца.   
###Line #    Mem usage    Increment   Line Contents
##================================================
##    10   14.547 MiB   14.547 MiB   @profile
##    11                             def merge(left, right):
##    12
##    13   14.547 MiB    0.000 MiB       lst = []
##    14   14.547 MiB    0.000 MiB       while left and right:
##    15   14.547 MiB    0.000 MiB           if left[0] < right[0]:
##    16   14.547 MiB    0.000 MiB               lst.append(left.pop(0))
##    17                                     else:
##    18   14.547 MiB    0.000 MiB               lst.append(right.pop(0))
##    19   14.547 MiB    0.000 MiB       if left:
##    20   14.547 MiB    0.000 MiB           lst.extend(left)
##    21   14.547 MiB    0.000 MiB       if right:
##    22   14.547 MiB    0.000 MiB           lst.extend(right)
##    23   14.547 MiB    0.000 MiB       return lst
##
##
##Filename: task2.py
##
##Line #    Mem usage    Increment   Line Contents
##================================================
##    24   14.547 MiB   14.547 MiB   @profile
##    25                             def mergesort(lst):
##    26
##    27
##    28   14.547 MiB    0.000 MiB       length = len(lst)
##    29   14.547 MiB    0.000 MiB       if length >= 2:
##    30   14.547 MiB    0.000 MiB           mid = int(length / 2)
##    31   14.547 MiB   14.547 MiB           lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
##    32   14.547 MiB    0.000 MiB       return lst
##
##
##Filename: task2.py
##
##Line #    Mem usage    Increment   Line Contents
##================================================
##    33   14.547 MiB   14.547 MiB   @profile
##    34                             def sort_python(lst):
##    35   14.547 MiB    0.000 MiB       return sorted(lst)
