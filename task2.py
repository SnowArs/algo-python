##Написать два алгоритма нахождения i-го по счёту простого числа.
##Без использования «Решета Эратосфена»;
##Используя алгоритм «Решето Эратосфена»
##Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
##Результаты анализа сохранить в виде комментариев в файле с кодом.

import timeit

def not_eratosfen():
    num = 100
    data = [2]
    check = 0
    n = 3
    sum_num = 0

    while sum_num < num-1:

        for i in range(2, n):
            if n % i == 0 and i != n:
                check = 0
                break
            else:
                check += 1
            sum_num += 1
        if check > 0:
            data.append(n)
        check = 0
        n += 1

    return data

# алгоритм взял из методички
def eratosfen():

    n = 100
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


print(timeit.timeit("not_eratosfen()", setup="from __main__ import not_eratosfen", number = 100000))
print(timeit.timeit("eratosfen()", setup="from __main__ import eratosfen", number = 100000))

##результаты:

##====== RESTART: C:\Users\membe\Desktop\geek\алгоритмы\lesson4\task2.py ======
##2.73020808
##3.6020770939999998
##>>> 
##====== RESTART: C:\Users\membe\Desktop\geek\алгоритмы\lesson4\task2.py ======
##2.672232349
##5.430583443 - странное большое число
##>>> 
##====== RESTART: C:\Users\membe\Desktop\geek\алгоритмы\lesson4\task2.py ======
##2.667635662
##3.7094001280000004
#===============================================================
#на 100000 циклах cProfile тоже показал не большие различия между алгоритмами:

##ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##        1    0.057    0.057    0.057    0.057 2profile.py:33(eratosfen)
##        1    0.000    0.000    0.093    0.093 2profile.py:64(main)
##        1    0.035    0.035    0.035    0.035 2profile.py:9(not_eratosfen)
##        1    0.000    0.000    0.093    0.093 <string>:1(<module>)
##        1    0.000    0.000    0.093    0.093 {built-in method builtins.exec}
##     9781    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
##        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

## могу предположить, что создание нулевого массива, заполнение его числамми, и последующй его постоянный перебор в методе eratosfen несколько более затратно,
#чем поиск числа и добавление его к массиву как в методе not_eratosfen
