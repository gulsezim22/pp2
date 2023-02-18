a, b=5, 20
list1 = [i for i in range(a,b+1)]
list2 = [i*i for i in list1]
print(list2)
for i in range(a,b+1):
    print(i*i)