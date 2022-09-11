some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
print(some_list)
summa = 0
for i in range(0,len(some_list),2):
    summa += int(some_list[i])
print(summa)
