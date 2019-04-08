#Найти максимальный элемент среди минимальных элементов столбцов матрицы


import random

@profile
def my_func():
        array = [[random.randint(1, 100) for i in range(500)] for j in range(500)]

##        for line in array: 
##                for j in line:
##                        print(j, end = ' ')
##                print()
##                
##        print('-'* 8)

        for i in range(500):
                min = array[0][i]
                for j in range(500):
                        if min > array[j][i]:
                                min = array[j][i]
##                print(min, end=' ')
##        print()

if __name__ == '__main__':
   my_func()

# версия Python - 3.7, Win - 64
# что и следовало ожидать,  существенное увеличение массива отразилось на занимаемой программой памяти

   
##Line #    Mem usage    Increment   Line Contents
##================================================
##     6   14.625 MiB   14.625 MiB   @profile
##     7                             def my_func():
##     8   14.625 MiB    0.000 MiB           array = [[random.randint(1, 100) for i in range(20)] for j in range(20)]
##     9
##    10   14.629 MiB    0.000 MiB           for line in array:
##    11   14.629 MiB    0.000 MiB                   for j in line:
##    12   14.629 MiB    0.000 MiB                           print(j, end = ' ')
##    13   14.629 MiB    0.004 MiB                   print()
##    14
##    15   14.629 MiB    0.000 MiB           print('-'* 8)
##    16
##    17   14.629 MiB    0.000 MiB           for i in range(20):
##    18   14.629 MiB    0.000 MiB                   min = array[0][i]
##    19   14.629 MiB    0.000 MiB                   for j in range(20):
##    20   14.629 MiB    0.000 MiB                           if min > array[j][i]:
##    21   14.629 MiB    0.000 MiB                                   min = array[j][i]
##    22   14.629 MiB    0.000 MiB                   print(min, end=' ')
##    23   14.629 MiB    0.000 MiB           print()

##Line #    Mem usage    Increment   Line Contents
##================================================
##     6   14.574 MiB   14.574 MiB   @profile
##     7                             def my_func():
##     8   15.711 MiB    0.129 MiB           array = [[random.randint(1, 100) for i in range(500)] for j in range(500)]
##     9
##    10                             ##        for line in array:
##    11                             ##                for j in line:
##    12                             ##                        print(j, end = ' ')
##    13                             ##                print()
##    14                             ##
##    15                             ##        print('-'* 8)
##    16
##    17   15.750 MiB    0.000 MiB           for i in range(500):
##    18   15.750 MiB    0.000 MiB                   min = array[0][i]
##    19   15.750 MiB    0.012 MiB                   for j in range(500):
##    20   15.750 MiB    0.016 MiB                           if min > array[j][i]:
##    21   15.750 MiB    0.000 MiB                                   min = array[j][i]
