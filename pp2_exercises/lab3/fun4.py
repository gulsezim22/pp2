def prime(n): 
    if n == 1: 
        return False
    elif n <= 0: 
        return False 
    for i in range(2, n): 
        if n%i == 0: 
            return False 
    return True 
def filter_prime(arr): 
	prime_arr =[ ] 
	for i in arr: 
		x = prime(i) 
		if x == True: 
			prime_arr.append(i) 
	return prime_arr 
