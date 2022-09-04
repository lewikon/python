#task 2
num = []
count = 0
while (count < 5):
    a = int(input('number: '))
    num.append(a)
    count = count + 1
print(num)
max = num[0]
for i in num:
    if (i>max):
        max = i
print (max)