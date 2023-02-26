import re

x = str(input())

def Func(y):
    w = '[A-Z]+[a-z]+$'
    if re.search(w,y):
        return "YES"
    else:
        return "NO"

print(Func(x))