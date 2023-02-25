import re
def insertspace(s1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", s1)

print(insertspace("TgvgYhvhzx"))
print(insertspace("djcj"))