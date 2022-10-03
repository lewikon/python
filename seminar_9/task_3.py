def thesaurus(*args):
    dict = {}
    for i in args:
        if i[0]in dict.keys():
            dict[i[0]].append(i)
        else:
            dict[i[0]] = []
            dict[i[0]].append(i)
    return dict
print(thesaurus('Илья','Инна','Надежда','Любовь','Николай'))