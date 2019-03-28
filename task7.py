#В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

array = [random.randint(-15, 15) for i in range(1, 11)]
min = array[0]
count = 0

print('исходный массив из 10 случайных чисел:\n', array)

for i in array:
	if min > i:
		min = i

for s in array:
	if s != min:
		min_2 = s 
		break
		
for n in array:
	if n == min:
		count +=1
		if count > 1:
			break
	elif n < min_2:
		min_2 = n
		


print(f'минимальное значение {min}, встречается миниму {count} разa' if count > 1 else f'минимальное значение {min}, второй наименьший элемент {min_2}')

