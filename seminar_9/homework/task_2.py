my_dict = {'first one': 'we can do it'}

def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(lala = '12',lapa ='13',jojo='14')
print(my_dict)