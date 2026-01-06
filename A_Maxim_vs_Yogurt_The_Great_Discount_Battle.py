t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    c = min(2 * a, b)
    if n % 2 == 0:
        cost = (n // 2) *c
    else:
        cost = (n // 2) * c + a
    print(cost)
