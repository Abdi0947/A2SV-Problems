t=int(input())
for _ in range(t):
    x=int(input())
    if x==1:
        print(3)
    else:
        low=x&-x
        if x&(x-1)==0:
            print(x+1)
        else:
            print(low)