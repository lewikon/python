
def to_dict(lst):
    some_dict = {}
    for i in lst:
        some_dict[i] = i
    return some_dict

some_list = list(input('введите  значения через запятую: ').split(','))
print(to_dict(some_list))