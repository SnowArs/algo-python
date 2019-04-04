#Пользователь вводит данные о количестве предприятий, их наименования
#и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
#Программа должна определить среднюю прибыль (за год для всех предприятий)
#и вывести наименования предприятий, чья прибыль выше среднего и отдельно
#вывести наименования предприятий, чья прибыль ниже среднего.

import collections

i = 1
profit_sum = 0
zavod =[]
zavod_infa =[]

mill = collections.namedtuple('mill', ['name', 'profit'])
num = input('введите количество предприятий :')

while i <= int(num):
	mill_name = input(f'введите название фабрики под номером {i} :')
	zavod.append(mill_name)
	i += 1

for n in zavod:
		quoter1 = int(input(f'введите прибыль 1го квартала по фабрике {n}, kUSD :'))
		quoter2 = int(input(f'введите прибыль 2го квартала по фабрике {n}, kUSD : '))
		quoter3 = int(input(f'введите прибыль 3го квартала по фабрике {n}, kUSD : '))
		quoter4 = int(input(f'введите прибыль 4го квартала по фабрике {n}, kUSD : '))
		p = mill(n, quoter1 + quoter2 + quoter3 + quoter4)
		zavod_infa.append(p)
		profit_sum = p.profit	+ profit_sum
		
average_profit = profit_sum/len(zavod)

for i in zavod_infa:
	print()
	print(f'Годовая прибыль завода "{i[0]}" составляет {i[1]}kUSD - это меньше средней '
	f'прибыли (за год для {num}х предприятий)-{round(average_profit, 1)}kUSD'
        if i[1] < average_profit else f'Годовая прибыль завода "{i[0]}" составляет {i[1]}kUSD'
        f'- это больше средней прибыли (за год для '
	f'{num}х предприятий)-{round(average_profit, 1)}kUSD')


