t = int(input())
for _ in range(t):
    n=int(input())
    pages=list(map(int,input().split()))
    first=pages.pop()
    m=max(pages)
    print(first+m)
