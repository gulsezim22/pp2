def palindrome(s):
    n=len(s)
    c=False
    if(s==s[::-1]):
        c=True
    print(c)