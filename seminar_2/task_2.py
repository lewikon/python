from operator import le


n = int(input('number: '))
array = []
for i in range(1,n+1):
    i = 3*i+1
    array.append(i)
print (array)
len = ''
a = 1
for i in array:
    len += str(a) + ':' + str(i) + ' '
    a += 1
print(len)