from array import array
from random import randint, random


n = int(input('number: '))
array = []
for i in range(n):
    a = (-3)**i
    array.append(a)
print (*array, sep=', ')