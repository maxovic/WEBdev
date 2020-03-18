arr = list(map(int, input().split()))
def MIN4X(a, b, c, d):
    return min(a, min(b, min(c, d)))

print(MIN4X(arr[0], arr[1], arr[2], arr[3]))