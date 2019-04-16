from itertools import permutations
import hashlib

num = 0
comb = []
string = input('ВВЕДИТЕ СТРОКУ из маленьких неповторяющихся латинских букв  :')

for i in range(1, (len(string)+1)):

    for i in permutations(string, i):
        num +=1
        s = ''.join(i)
        print(f'{num} - номер подстроки для комбинации {s}, ее хеш   - ', end = "")
        hesh = hashlib.sha1(bytes(s.encode('utf-8'))).hexdigest()
        print(hesh)
        comb.append(hesh)
print(f'итого количество комбинаций - {num}')
print(f'количество уникальных комбинаций хеша -', len(set(comb)))



