n = int(input())
res = int(input())
arr = []
ok = True

while(n):
    arr.append(n % 10)
    n = int(n / 10)
if(len(arr) != 4):
    ok = False
if(ok):
    if(arr[0] != arr[3] | arr[1] != arr[2]):
        ok = False

if(ok):
    if(res == 1):
        print("YES")
    else:
        print("NO")
else:
    if(res == 1):
        print("NO")
    else:
        print("YES")