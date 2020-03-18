import math
n = int(input())
res = 0
temp = 1

while(temp < n):
    temp *= 2
    res = res + 1

print(res)
