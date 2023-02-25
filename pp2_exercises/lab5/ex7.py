import re
def snaketocamel(text):
        return ''.join(x.capitalize() or '_' for x in text.split('_'))

print(snaketocamel('chh_uzx_hjj'))
