num = int(input('введите номер четверти: '))
if (num == 1):
    print('x > 0; y > 0')
elif (num == 2):
    print('x < 0; y > 0')
elif (num == 3):
    print('x < 0; y < 0')
elif (num == 4):
    print('x > 0; y < 0')
else:
    print('введите число от 1 до 4')