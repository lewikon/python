from sympy import *

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
# x, y = symbols('x y')
# result = solveset(Eq(x ** 2 * a + b * x + c,0),x)
# print(result)
dis = b**2  - 4*a*c
if(dis < 0):
    print('no roots')
if dis == 0:
    result = ((-b + dis ** (1/2)) / (2*a))
    print(result)
if dis > 0:
    result_pos = ((-b + dis ** (1/2)) / (2*a))
    print(result_pos)
    result_neg = ((-b - dis ** (1/2)) / (2*a))
    print(result_neg)
