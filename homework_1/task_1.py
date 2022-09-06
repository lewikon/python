day = int(input('Введите номер дня недели: '))
if (day > 0 and day <6):
    print('Это будний день')
elif(day > 5 and day < 8):
    print('Это выходной')
else:
    print('В неделе 7 дней')