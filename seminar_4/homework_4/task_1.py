a = input('Введите число: ')
b = input('Введите точность числа: ')
number = a.split('.')
result = b.split('.')
n_count = len(number[1])
r_count = len(result[1])
if(n_count == r_count):
    print(a)
if(n_count>r_count):
    kk = float(a)
    print(round(kk,r_count))
if(n_count<r_count):
    print(a+'0'*(r_count-n_count))

