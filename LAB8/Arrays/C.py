n = int(input())
arr = list(map(int, input().split()))
res = 0
for i in range(0, n):
    if(arr[i] > 0):
        res = res + 1
print(res)