import re

x = str(input())

def Func(y):
    w = 'ab{2,3}'
    if re.search(w,y):
        return "YES"
    else :
        return "NO"

print(Func(x))