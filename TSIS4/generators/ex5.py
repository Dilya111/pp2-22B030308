N = int(input())

def qwe(n):
    while n>=0:
        yield n
        n -= 1
for i in qwe(N):
    print(i)