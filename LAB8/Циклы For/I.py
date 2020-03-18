import math
n = int(input())
arr = []

for i in range(1, int(math.sqrt(n)) + 1):
    if(n % i == 0):
        a = i
        b = n / i
        if(a != b):
            arr.append(a)
            arr.append(b)
        else:
            arr.append(a)
print(len(arr))