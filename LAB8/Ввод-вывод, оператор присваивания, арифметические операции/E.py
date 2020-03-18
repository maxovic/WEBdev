v = int(input())
t = int(input())

S = v * t
if(v == 0 | t == 0):
    print(0)
elif(S > 0):
    print(S % 109)
else:
    S = S % 109
    S = S + 109
    S = S % 109
    print(S)