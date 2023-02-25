import re
def matching(s):
        s2 = '^a(b){2,3}$'
        if re.search(s2,  s):
                return True
        else:
                return False
print(matching("a"))
print(matching("abb"))