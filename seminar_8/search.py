def search(user_list):
    request = input('Введите данные для поиска: ')
    t = True
    for i in user_list:
        if i['LastName'] == request or i['Name'] == request or i['Number'] == request: 
            print(*i.values())
        t = False
        if t:
            print('Информации нет, проверьте правильность ввода')