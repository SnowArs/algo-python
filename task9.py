#Найти максимальный элемент среди минимальных элементов столбцов матрицы


import random

array = [[random.randint(1, 100) for i in range(4)] for j in range(4)]

for line in array: 
	for j in line:
		print(j, end = ' ')
	print()
	
''''for line in array:
	for i, item in enumerate(line):
		print(i, item)
		min'''
print('-'* 8)

# не совсем понял задание, поэтому нашел просто самый маленький элемент в столбце
for i in range(4):
	min = array[0][i]
	for j in range(4):
		if min > array[j][i]:
			min = array[j][i]
	print(min, end=' ')
print()
