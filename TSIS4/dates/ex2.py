import datetime

d1 = datetime.datetime.today()
print(d1)

d2 = d1 - datetime.timedelta(days = 1)
print(d2)

d3 = d1 + datetime.timedelta(days = 1)
print(d3)