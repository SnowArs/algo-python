#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

array = [random.randint(-5, +5) for i in range(1, 11)]
index_max_low  = count = count_more = 0

print('исходный массив из 10 случайных чисел:\n', array)

for i in array:
    if i < 0:
        max_low = i
        index_max_low = count
        break
    count += 1        

for i in array:
    if 0 > i > max_low:
        max_low = i
        if count_more > count:
            index_max_low = count_more
    count_more += 1

print(f'максимальный отрицательный элемент-({max_low}), порядковый номер в массиве: {index_max_low}, начиная с 0')
