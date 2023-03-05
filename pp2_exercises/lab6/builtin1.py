from functools import reduce
list1 = [5, 1, 3]
def multiply(list1):
    result1 = reduce((lambda x, y: x * y), list1)
    return result1
print(multiply(list1))
   
