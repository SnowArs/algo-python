#Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

import random

array = [[random.randint(1, 5) for i in range(4)] for j in range(4)]

for line in array: 
	for j in line:
		print(j, end = ' ')
	print()
last_row = input('введите последние элемнты для каждой из 4 строк через пробел :\n')

n = 0
for i in last_row.split():
	array[n].append(int(i))
	n += 1
print()
sum_line = 0
for line in array:
	for m in line:
		sum_line += m
		print(m, end = ' ')
	print(' |', sum_line)
	sum_line = 0
