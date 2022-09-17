
from sympy import symbols
from random import *
k = int(input('введите k: '))
x = symbols('x')
some_str = ''
while(k > 1):
    some_str += str(int(random()*100 + 1)) + 'x' + '^' + str(k) + ' + '
    k -= 1
some_str += str(int(random()*100 + 1)) + 'x + '
some_str += str(int(random()*100 + 1))
with open('result.txt', 'w') as r:
    r.write(some_str)
