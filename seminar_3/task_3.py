some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
some_str = input('Введите строку: ')
try:
    print(some_list.index(some_str, some_list.index(some_str) + 1))
except:
    print(-1)