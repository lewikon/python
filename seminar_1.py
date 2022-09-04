#task 1
a = int (input('введите первое число '))
b = int (input('введите второе число '))
if (a == b*b):
    print('{} явлется квадратом {}'.format(a,b))
elif  (b == a*a):
    print('{} явлется квадратом {}'.format(b,a))
else:
    print('нет')
