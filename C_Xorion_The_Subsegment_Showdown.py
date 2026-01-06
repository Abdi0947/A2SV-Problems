t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    diff = x ^ y
    maxm = diff&-diff
    print(maxm)
