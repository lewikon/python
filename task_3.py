n = int(input('number: '))
m = n * -1
if (n < 0):
    print (n)
    while(n < m):
        n = n+1
        print(n)
elif (n > 0):
    print(n)
    while(n > m):
        n = n-1
        print(n)
else:
    print(n)