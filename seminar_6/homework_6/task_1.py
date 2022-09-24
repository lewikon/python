def in_two_lists(some_sting, ops=('-', '+', '*', '/')):
    operators = []
    numbers = []
    temp = ''
    for i in some_sting:
        if not i in ops:
            temp += i
        else:
            operators.append(i)
            numbers.append(float(temp))
            temp = ''
    numbers.append(float(temp))
    while len(numbers) > 1:
        if '*' in operators:
            index = operators.index('*')
            temp = calc(numbers[index], numbers[index + 1], '*')
            numbers[index] = temp
        elif '/' in operators:
            index = operators.index('/')
            temp = calc(numbers[index], numbers[index + 1], '/')
            numbers[index] = temp
        elif '+' in operators:
            index = operators.index('+')
            temp = calc(numbers[index], numbers[index + 1], '+')
            numbers[index] = temp
        elif '-' in operators:
            index = operators.index('-')
            temp = calc(numbers[index], numbers[index + 1], '-')
            numbers[index] = temp
        del (numbers[index + 1])
        del (operators[index])
    return numbers[0]

def calc(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number
    if operator == '/':
        return first_number / second_number

some_string = input('Введите: ')
ops = ['-', '+', '*', '/']
print(in_two_lists(some_string,ops))