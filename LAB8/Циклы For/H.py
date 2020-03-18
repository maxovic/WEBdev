import math
n = int(input())
dels = []
for i in range(1, n + 1):
    if(n % i == 0):
        dels.append(i)

for x in dels:
    print(x)

