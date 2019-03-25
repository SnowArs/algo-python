the_list = []
s = 0
number = input("введите натуральное число :")

for i in number:
    the_list.append(0)
for i in number:
    s +=1
    the_list[len(number) - s] = i

print(the_list)
