t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    if n==1:
        print(-1)
        continue
    average_wealth=sum(a)/n
    threshold=sum(a)/2
    
