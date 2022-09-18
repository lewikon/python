txt_find = 'абв'
some_string = ''
with open('task_1.txt', 'r') as task:
    for line in task:
        some_string +=line + ' '
new_text = [j for j in some_string.split() if txt_find not in j]
new_string = ''
for i in range(0,len(new_text)):
    new_string += new_text[i] + ' ' 
print(new_string)
