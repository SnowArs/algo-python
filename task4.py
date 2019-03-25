i = 1
a = 1
data = 0
number = int(input("введите количество элемнтов ряда 1, -0.5, 0.25, -0.125, ...  :"))

while i <= number:
    data += a
    a = a/-2
    i +=1
    
print(data)
    

