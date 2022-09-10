from array import array
from random import randint, random


n = int(input('number: '))
i = 0
array = []
while(i < n):
    a = randint(-100,100)
    array.append(a)
    i = i+1
print (array)