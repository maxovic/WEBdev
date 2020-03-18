arr = list(map(int, input().split()))

def powa(a, k):
    cur = 1
    if(k == 0):
        return cur
    else:
        for i in range(1, k + 1):
            cur *= a
        return cur

print(powa(arr[0], arr[1]))