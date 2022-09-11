some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
print(some_list)
some_new_list = []
if len(some_list) % 2 == 0:
    for i in range(0,len(some_list)//2):
        a = int(some_list[i])
        b = int(some_list[len(some_list)-1-i])
        c = a * b
        some_new_list.append(c)
    print(some_new_list)
else:
    for i in range(0,len(some_list)//2):
        a = int(some_list[i])
        b = int(some_list[len(some_list)-1-i])
        c = a * b
        some_new_list.append(c)
    d = int(some_list[len(some_list)//2])**2
    some_new_list.insert(len(some_list)//2,d)
    print(some_new_list)