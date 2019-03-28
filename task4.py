#Определить, какое число в массиве встречается чаще всего.

import random
n=0
s=0
count_max = 0
count = 1

array = [random.randint(1, 10) for i in range(1, 20)]
print('исходный массив из 20 случайных чисел:\n', array)

for i in array:
	
	for j in array:
		if i == j and n != s:
			count +=1
		s += 1
	n +=1
	
	if count_max < count:
		count_max = count
		often = i
	count = 0
print(f'чаще всего встречается число {often}, в количестве {count_max} раз/а')
		
