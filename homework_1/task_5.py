from cmath import sqrt

first_x = int(input('x1: '))
first_y = int(input('y1: '))
second_x = int(input('x2: '))
second_y = int(input('y2: '))
dist = round(((first_x-second_x)**2 + (first_y-second_y)**2)**(1/2),ndigits=3)
print(dist)