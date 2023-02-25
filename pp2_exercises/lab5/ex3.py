import re
def underscorel(s1):
        s2 = '^[a-z]+_[a-z]+$'
        if re.search(s2,  s1):
                return 'Found'
        else:
                return('Not found')

print(underscorel("sjdfjh_sv"))
print(underscorel("TvgsvT_hsg"))
