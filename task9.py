#алгоритм аналогичен заданию 7
number1 = input("введите 1е число :")
number2 = input("введите 2е число :")
number3 = input("введите 3е число :")

if (number1 < number2 < number3) | (number3 < number2 < number1): print("средним является ", number2)
elif (number2 < number1 < number3) | (number3 < number1 < number2): print("средним является ", number1)
elif (number2 < number3 < number1) | (number1 < number3 < number2): print("средним является ", number3)
else:
    print("несколько чисел равны")


