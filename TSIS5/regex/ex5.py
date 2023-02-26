import re
x = str(input())

def Func(y):
    w = 'a.*?b$'
    if re.search(w,y):
        return "YES"
    else :
        return "NO"

print(Func(x))
