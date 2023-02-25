import re
s2=input()
print(re.findall('[A-Z][^A-Z]*', s2))
