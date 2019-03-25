max = 0
sum = 0 
the_list = []
while 1:
    number = int(input("Введите число или 0 если остановить :"))
    if number != 0:
        the_list.append(number)
    else:
        break

for i in the_list:
    if i > max:
        max = i

for i in str(max):
    sum =sum + int(i)
print(f"самое большое число из введенных - {max}, сумма цифр, входящих в число  = {sum}")
