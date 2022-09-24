some_string = list((input('введите список чисел: ')).split(','))
new_list = list(set(some_string))
print(sorted(new_list))