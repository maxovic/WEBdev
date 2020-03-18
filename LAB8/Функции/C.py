arr = list(map(int, input().split()))

def XOR(a, b):
    if(a == 0):
        if(b == 1):
            return 1
        else:
            return 0
    else:
        if(b == 1):
            return 0
        else:
            return 1

print(XOR(arr[0], arr[1]))