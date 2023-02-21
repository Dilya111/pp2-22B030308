a = int(input())
b = int(input())

def squares(a,b):
    while a<=b:
        yield a*a
        a+=1
 
for i in squares(a, b + 1):
  print(i)

