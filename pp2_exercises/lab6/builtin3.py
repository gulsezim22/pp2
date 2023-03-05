def palindrome(s):
    s=s.casefold()
    s2=reversed(s)
    if(list(s)==list(s2)):
        return True
    else:
        return False
    
print(palindrome("aseresa"))