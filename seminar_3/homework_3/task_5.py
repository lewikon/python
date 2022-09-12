size = int(input('number: '))
fib = [0,1]
for i in range(2,size):
    a = fib[i-1]+fib[i-2]
    fib.append(a)
del fib[:2]
neg_fib = [1,0]
for i in range(2,size):
    a = neg_fib[i-2] - neg_fib[i-1]
    neg_fib.append(a)
for i in neg_fib:
    fib.insert(0,i)
print(fib)