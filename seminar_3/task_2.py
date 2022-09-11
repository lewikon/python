from curses.ascii import isdigit

some_list = input('введите строки через запятую: ').split(',')
print(some_list)
n = input('введите искомое число: ')
for i in some_list:
    if n in i:
        print('yes')
    else:
        print('no')

# some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
# n = int(input('Введите число: '))
# if str(n) in some_list:
#     print('Да')
# else:
#     print('Нет')