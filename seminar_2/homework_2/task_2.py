n = int(input())
number = 1
array = []
for i in range(1,n+1):
    number *= i
    array.append(number)
print(*array, sep=',')
