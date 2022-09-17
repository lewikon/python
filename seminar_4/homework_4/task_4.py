
from sympy import symbols
from random import *
k = int(input('введите k: '))
x = symbols('x')
some_str = ''
while(k > 1):
    some_str += str(int(random()*100)) + 'x' + '^' + str(k) + ' + '
    k -= 1
some_str += str(int(random()*100)) + 'x + '
some_str += str(int(random()*100))
print(some_str)