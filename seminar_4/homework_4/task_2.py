from distutils.command.build_scripts import first_line_re


a = int(input('введите число: '))
first_list = []
for i in range(2,a+1):
    if(a%i == 0 ):
        first_list.append(i)
print(first_list)
second_list = []
for i in first_list:
    lol = 0
    for j in range(2,i):
        if i%j == 0:
            lol += 1
    if lol == 0:
        second_list.append(i)
print(second_list)
