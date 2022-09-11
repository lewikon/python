import time
print(str(time.time()).split('.')[-1])
a = int(str(time.time()).split('.')[-1])
start = int(input())
end = int(input())
print(a % (end - start) + start)