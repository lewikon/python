path = 'data.txt'
with open ('data.txt', 'a') as d:
    info = input('Введите новые данные:')
    d.write(info)


