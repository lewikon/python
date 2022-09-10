from operator import le


n = int(input('number: '))
some_dict = {}
for i in range(1,n+1):
    some_dict[i] = 3*i+1
print(some_dict)