import re

x = str(input())

def Function(y):
    return re.sub(r"(\w)([A-Z])",r"\1 \2",y)

print(Function(x))
