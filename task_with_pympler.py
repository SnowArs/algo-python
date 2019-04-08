##Написать два алгоритма нахождения i-го по счёту простого числа.
##Без использования «Решета Эратосфена»;
##Используя алгоритм «Решето Эратосфена»

from pympler import asizeof
import sys 


num = 100
data = [2]
check = 0
s = 3
sum_num = 0

while sum_num < num-1:

    for i in range(2, s):
        if s % i == 0 and i != s:
            check = 0
            break
        else:
            check += 1
        sum_num += 1
    if check > 0:
        data.append(s)
    check = 0
    s += 1



n = 100
a = [0] * n  # создание массива с n количеством элементов
for _ in range(n):  # заполнение массива ...
    a[_] = _  # значениями от 0 до n-1

a[1] = 0

m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
while m < n:  # перебор всех элементов до заданного числа
    if a[m] != 0:  # если он не равен нулю, то
        j = m * 2  # увеличить в два раза (текущий элемент - простое число)
        while j < n:
            a[j] = 0  # заменить на 0
            j = j + m  # перейти в позицию на m больше
    m += 1

b = []
for o in a:
    if a[o] != 0:
        b.append(a[o])
#del a

# версия Python - 3.7, Win - 64
print("память затраченная на переменные в алгоритме 1")
print(f'"num" - {asizeof.asizeof(num)}, "data"-{asizeof.asizeof(data)}, "_"-{asizeof.asizeof(check)},'
      f' "s"-{asizeof.asizeof(s)}, "sum_num"-{asizeof.asizeof(sum_num)}, "i"-{asizeof.asizeof(i)}')
print('ИТОГО, память затраченная на переменные по алгоритму 1 :', asizeof.asizeof(num)+ asizeof.asizeof(data)+
      asizeof.asizeof(check)+ asizeof.asizeof(s)+asizeof.asizeof(sum_num)+asizeof.asizeof(i))
print()
print("память затраченная на переменные в алгоритме 2")
print(f'"n" - {asizeof.asizeof(n)}, "a"-{asizeof.asizeof(a)}, "_"-{asizeof.asizeof(_)},'
      f' "m"-{asizeof.asizeof(m)}, "j"-{asizeof.asizeof(j)}, "b"-{asizeof.asizeof(b)}, "o"-{asizeof.asizeof(o)}')
print('ИТОГО, память затраченная на переменные по алгоритму 2 :', asizeof.asizeof(n)+ asizeof.asizeof(a)+
      asizeof.asizeof(_)+ asizeof.asizeof(m)+asizeof.asizeof(j)+asizeof.asizeof(b)+asizeof.asizeof(o))
print("если в конце программы удалить не нужный массив 'a', то это существенно сократит расход памяти :", asizeof.asizeof(n)+
      asizeof.asizeof(_)+ asizeof.asizeof(m)+asizeof.asizeof(j)+asizeof.asizeof(b)+asizeof.asizeof(o))
