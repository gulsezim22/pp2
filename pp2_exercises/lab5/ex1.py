import re
def matching(s):
        s2 = '^a(b*)$'
        if re.search(s2,  s):
                return True
        else:
                return False
print(matching("a"))
print(matching("abbbb"))