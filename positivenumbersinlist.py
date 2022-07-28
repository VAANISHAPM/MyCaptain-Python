mylist = []
n = int(input("Input size of the list "))
for i in range(0, n):
    p = int(input())
    mylist.append(p)
    
for i in mylist:
    if i >= 0:
       print(i, end = ", ")
