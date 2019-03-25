cont = 1
while cont:
       
    if int(cont) != 0:
        number1 = int(input("введите число 1 :"))
        number2 = int(input("введите число 2 :"))
        move = input("введите желаемое действие '+' '-' '*' '/' :")
        
        if move in '+-*/':
            if move == "+":
                print("сумма чисел =", number1+number2)
            if move == "-":
                print("разность чисел =", number1-number2)
            if move == "*":
                print("произведение чисел =", number1*number2)
            if move == "/":
                if number2 == 0:
                    print("на 0 делить нельзя")
                else:
                    print("частное чисел =", number1/number2)
        else:
            print("введите правильный оператор")
    else:
        break
    cont = input("Если не хотите продолжать введите 0 или введите любое число :")

print("до свидания")
