def histogram(list1):
    s=""
    for i in list1:
        for j in range(0,i):
            s+="*"
        print(s)
        s=""