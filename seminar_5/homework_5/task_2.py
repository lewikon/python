from random import *
condit = []
with open('task_2.txt', 'r') as task:
    for line in task:
        condit.append([int(x) for x in line.split()])
candys, one_step = condit[0]
print('Число конфет: {}, максимальное количество за шаг: {}'.format(candys,one_step))
turn = randint(1,2)
print('Вы ходите: {}'.format(turn))

while(candys>0):
    if turn == 2:
        candys -= (candys % (one_step+1))
        print('Ход сделан, осталось {} конфет.'.format(candys))
        turn -= 1
        if candys == 0:
            break
    if turn == 1:
        opp_step = int(input('Ваш ход: '))
        candys -= opp_step
        print('Ход сделан, осталось {} конфет.'.format(candys))
        turn += 1
        if candys == 0:
            break
print('Победил участник {}'.format(turn))