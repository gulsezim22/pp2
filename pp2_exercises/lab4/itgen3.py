def divisible(n):
    a = [i for i in range(0,int(n)+1)]
    b = [i for i in a if i%3==0 or i%4==0]
    print(b)