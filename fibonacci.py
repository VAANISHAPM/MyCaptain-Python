n = int(input())
f = 0
f1 = 1
if n <= 0:
    print(f)
else:
    print(f, f1, end = " ")
    for i in range (2, n):
        temp = f + f1                           
        print(temp, end = " ")
        f = f1
        f1 = temp
