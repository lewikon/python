a = float(input('number: '))
result = int(a*10%10)
print(result)

number = input()
if '.' in number:
    print(number[number.index('.')+1])
