def permutation(s, i=0):
    if i == len(s):   	 
        print("".join(s))
    for j in range(i, len(s)):
        perm = [element for element in s]#as array
        perm[i], perm[j] = perm[j], perm[i]
        permutation(perm, i + 1)
