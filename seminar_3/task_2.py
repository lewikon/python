from curses.ascii import isdigit


some_list = input('введите строки через запятую: ').split(',')
print(some_list)
n = input('введите искомое число: ')
for i in some_list:
    if n in i:
        print('yes')
    else:
        print('no')
