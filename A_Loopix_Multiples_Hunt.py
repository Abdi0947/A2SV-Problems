t = int(input())
for i in range(t):
    l, r, k = map(int, input().split())
    if k == 1:
        print(r - l + 1)
    else:
        max_x = r // k
        ops = max(0, max_x - l + 1)
        print(ops)
