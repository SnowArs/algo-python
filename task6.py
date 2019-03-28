#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(1, 100) for i in range(1, 11)]
min = max = array[0]
index_min = index_max = count = 0

print('исходный массив из 10 случайных чисел:\n', array)

for i in array:
	if min > i:
		min = i
		index_min = count
	if max < i:
		max = i
		index_max = count
	count += 1

summ = sum(array[index_min+1: index_max])

print(f'сумма элементов между min-{min} и max-{max} = :' +  (f'{sum(array[index_min+1: index_max])}' if index_min < index_max else f' {sum(array[index_max+1: index_min])}') )
