#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

array[index_min], array[index_max] = array[index_max], array[index_min]

print(f'измененный массив, где минимальное {min} и максимальное {max} поменяны местами(без учета повторяющихся элементов):\n', array)
