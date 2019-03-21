number = input("введите 3х зачное число :")
sum = 0
add = 1
if len(number) == 3:
    for dig in number:
        sum = int(dig) + sum
        add = int(dig) * add
    print(f"сумма чисел= {sum}, произведение числел = {add}")
else:
    print("вы ввели не правильное число")


