t = int(input())
for i in range(t):
    x1, x2, x3 = map(int, input().split())

    diff1 = abs(x1 - x2)
    diff2 = abs(x2 - x3)
    diff3 = abs(x1 - x3)
    max_diff = max(diff1, diff2, diff3)

    print(max_diff)