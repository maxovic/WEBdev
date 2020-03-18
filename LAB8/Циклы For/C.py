import math
a = int(input())
b = int(input())
for i in range(a, b + 1):
    numf = math.sqrt(i)
    numi = int(math.sqrt(i))
    if(numf == numi):
        print(str(i) + " ")

