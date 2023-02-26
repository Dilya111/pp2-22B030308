import re

x = str(input())

def Function(y):
    w = '^a(b*)$'
    if re.search(w,y):
        return ('YES')
    else :
        return ('NO')

print(Function(x))