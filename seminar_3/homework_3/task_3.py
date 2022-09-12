from tkinter import N


some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
print(some_list)
new_list = []
for i in some_list:
    a = i.split('.')[-1]
    a = '0.' + a
    b = float(a)
    new_list.append(b)
dif = round(max(new_list)-min(new_list),ndigits=3)
print(dif)   