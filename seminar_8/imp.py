path = 'data.txt'
def imp():
    with open ('data.txt', 'a') as d:
        info = input('Введите новые данные:')
        d.write(info)


