string = input()
cnt = 0
cnt1 = 0
for i in string:
    if i.isupper():
        cnt += 1
    else:
        cnt1 += 1
print(cnt, cnt1)