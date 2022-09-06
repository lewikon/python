x = input()
y = input()
z = input()
print(not(x or y or z) == (not x) and (not y) and (not z))
