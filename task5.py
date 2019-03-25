i = 32
n = 1

while i <= 127:
    print("%4d-%s" % (i,chr(i)), end='\n')
    i +=1
    n +=1
    if n%10 == 0:
        print()

