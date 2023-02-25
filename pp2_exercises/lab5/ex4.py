import re
def oneuppercase(s1):
        s2 = '[A-Z]+[a-z]+$'
        if re.search(s2,  s1):
                return 'Found'
        else:
                return('Not found')

print(oneuppercase("Rvxg"))
print(oneuppercase("TvgsvThsg"))