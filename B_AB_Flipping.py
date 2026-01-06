t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    res = 0
    used = [False] * n
    i = 0
    while i < n - 1:
        if s[i] == 'A' and s[i+1] == 'B' and not used[i] and not used[i+1]:
            res += 1
            used[i] = True
            used[i+1] = True
            i += 2
        else:
            i += 1
    print(res)