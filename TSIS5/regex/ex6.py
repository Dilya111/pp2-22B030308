import re

text = str(input())

w = (re.sub("[ ,.]", ":", text))

print(w)

