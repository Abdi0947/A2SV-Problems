t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    s = input().strip()
    whites = s[:k].count('W')
    recolor = whites
    for i in range(k, n):
        if s[i - k] == 'W':
            whites -= 1
        if s[i] == 'W':
            whites += 1
        recolor = min(recolor, whites)
    print(recolor)
