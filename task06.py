import random
i = 0
x = random.randrange(0, 100)

while i < 10:
	try_count = int(input(f'введите загаданное число, осталось {10 - i} попыток :'))
	if try_count < x:
		print('введеное число меньше загаданного')
	elif try_count > x:
		print('введеное число больше загаданного')
	else:
		print('поздравляем, вы угадали!')
		break
	i +=1

	if i == 10:
		print(f'к сожалению вы проиграли, загаданное число {x}')
