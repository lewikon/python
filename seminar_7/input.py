def txt_input(rad):
  with open('data.txt', 'r', encoding="utf-8") as f:
    num = f.readlines()
    user_list = []
    for i in num:
        txt_data = i.split()
        user_data = { 'LastName': txt_data[0],'Name': txt_data[1], 'Number': txt_data[2], 'Status': txt_data[3]}
        user_list.append(user_data)
  return user_list

path = 'data.txt'