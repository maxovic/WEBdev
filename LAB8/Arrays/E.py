n = int(input())
arr = list(map(int, input().split()))
res = "NO"
def sN(num):
    if(num > 0):
        return True
    else:
        return False
for i in range(1, n):
    if(sN(arr[i]) == sN(arr[i - 1])):
        res = "YES"
print(res)
