import math
from math import pi

def findarea(r):
    area= round(pi * (r**2),2)
    return area

def totaldue(money,tax):
    total=round(money+(money*tax),2)
    return total

def celsius(fahrenheit):
    cel= (fahrenheit-32) * (5/9)
    return cel

print(findarea(int(input())))
print(findarea(int(input())))
print(findarea(int(input())))
print(findarea(int(input())))
print(findarea(int(input())))

print(f"{totaldue(int(input()),float(input())):.2f}")
print(f"{totaldue(int(input()),float(input())):.2f}")
print(f"{totaldue(int(input()),float(input())):.2f}")

print(int(celsius(int(input()))))
print(f"{celsius(int(input())):.4f}")
print(f"{celsius(int(input())):.4f}")
print(f"{celsius(int(input())):.5f}")
