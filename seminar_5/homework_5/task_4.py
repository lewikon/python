from curses.ascii import isalpha


some_string = ''
with open('task_4.txt', 'r') as task:
    for line in task:
        some_string +=line + ' '
infor = [j for j in some_string]
print(some_string)

def short(line):
    counting = 1
    shorter_string = ''
    for i in range(0,len(line)-1):
        if line[i] == line[i+1]:
            counting += 1
        else:
            shorter_string += str(counting) + str(line[i])
            counting = 1
    return shorter_string

def long(line): 
    long_string = '' 
    count = '' 
    for i in line: 
        if not i.isalpha(): 
            count += i 
        else: 
            long_string += i * int(count) 
            count = '' 
    return long_string

print(short(some_string))
print(long(some_string))


