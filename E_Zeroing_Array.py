n=int(input())
a = list(map(int, input().split()))
total=sum(a)
max=max(a)
if total%2==0 and max <= total - max:
    print("YES")
else:
    print("NO")