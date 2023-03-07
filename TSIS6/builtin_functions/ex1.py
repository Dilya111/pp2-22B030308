def func(num):
    total = 1
    for i in num:
        total *= i
    return total
l = list(map(int,input().split()))
print(func(l))