from random import randint
some_list = [randint(0, 9) for i in range(10)]
print(some_list)

def count_it(sequence):
    num_dict = {int(i): sequence.count(i) for i in sequence}
    sorted_num = sorted(num_dict.items(), key=lambda element: element[1], reverse=False)
    return dict(sorted_num[-3:])

print(count_it(some_list))
