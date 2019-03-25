chet_list = []
nechet_list = []

number = input("введите натуральное число :")

for i in number:
    if int(i) % 2 == 0:
        chet_list.append(i)
    else:
        nechet_list.append(i)

print(f"четные числа :{chet_list}, нечетные числа {nechet_list}")
