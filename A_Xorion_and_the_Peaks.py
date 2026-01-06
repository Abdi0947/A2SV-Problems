t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=(n-1)//2
    if k > a:
        print(-1)
        continue
    values=list(range(1,n+1))
    for i in range(1, 2 * k, 2):
       values[i], values[i + 1] = values[i + 1], values[i]
    print(*values)