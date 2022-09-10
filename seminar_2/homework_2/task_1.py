n = list(input())
array = []
for i in n:
    if(i != '.'):
        array.append(int(i))
result = 0
for i in array:
    result += i
print(result)

