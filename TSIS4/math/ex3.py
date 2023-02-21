from math import tan, pi

numsides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = numsides * (length ** 2) / (4 * tan(pi / numsides))
print("The area of the polygon is: ",area)
