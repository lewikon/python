path = 'data.txt'
def exp(path):
    user_list = []
    with open (path, 'r') as d:
        info = d.readlines()
        for i in info:
            s_data  =  i.split()
            user_data = { 'LastName': s_data[0],'Name': s_data[1], 'Number': s_data[2], 'Status': s_data[3]}
            user_list.append(user_data)
    return user_list