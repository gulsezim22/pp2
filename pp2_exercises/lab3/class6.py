arr=[5,4,2,8,4,3]
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1))
filter_prime=list(filter(lambda x:is_prime(x)==True,arr))
print(filter_prime)