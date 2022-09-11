some_list = input('введите строки через запятую: ').split(',')
print(some_list)
n = str(input('введите искомое значение: '))
s_count = 0
for i in some_list:
    if i == n:
        s_count  += 1
    elif s_count == 2:
        print(some_list[i].index)
