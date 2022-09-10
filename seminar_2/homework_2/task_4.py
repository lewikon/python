from array import array
from random import random
from random import shuffle

array = []
for i in range(0,10):
    array.append(i)
shuffle(array)
print(array)
