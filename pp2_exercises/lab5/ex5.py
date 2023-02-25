import re
def atob(s1):
        s2 = 'a.*?b$'
        if re.search(s2,  s1):
                return 'Found'
        else:
                return('Not found')

print(atob("agcydgy-su7b"))
print(atob("TvgsvThsg"))