import numbers


n = int(input('number: '))
numbers = {}
for i in range(1,n+1):
    numbers[i] = (1+(1/i))**i
print(sum(numbers))