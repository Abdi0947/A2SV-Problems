t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    position = 0
    for i in range(n):
        position += a[i] + 1  # a[i] gaps + 1 for seat
    position -= 1  # circle adjustment
    if position <= m:
        print("YES")
    else:
        print("NO")
